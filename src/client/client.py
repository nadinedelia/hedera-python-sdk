import grpc
from src.outputs import token_service_pb2_grpc, crypto_service_pb2_grpc
from src.token.token_create_transaction import TokenCreateTransaction
from src.token.token_associate_transaction import TokenAssociateTransaction
from src.client.network import Network
from src.outputs import response_code_pb2
from src.utils import generate_transaction_id
import time

class Client:
    def __init__(self, network=None):
        if network is None:
            network = Network()
        self.network = network
        self.operator_account_id = None
        self.operator_private_key = None
        self.channel = grpc.insecure_channel(self.network.node_address)
        self.token_stub = token_service_pb2_grpc.TokenServiceStub(self.channel)
        self.crypto_stub = crypto_service_pb2_grpc.CryptoServiceStub(self.channel)

    def set_operator(self, account_id, private_key):
        self.operator_account_id = account_id.to_proto()
        self.operator_private_key = private_key

    def execute_transaction(self, transaction, timeout=60):
        transaction.transaction_id = generate_transaction_id(self.operator_account_id)
        transaction.node_account_id = self.network.node_account_id.to_proto()
        transaction.sign(self.operator_private_key)

        transaction_proto = transaction.to_proto()

        if isinstance(transaction, TokenCreateTransaction):
            response = self._submit_transaction_with_retry(transaction_proto, self.token_stub.createToken)
        elif isinstance(transaction, TokenAssociateTransaction):
            response = self._submit_transaction_with_retry(transaction_proto, self.token_stub.associateTokens)
        else:
            raise NotImplementedError("Transaction type not supported.")

        if response.nodeTransactionPrecheckCode != response_code_pb2.ResponseCodeEnum.OK:
            error_code = response.nodeTransactionPrecheckCode
            error_message = response_code_pb2.ResponseCodeEnum.Name(error_code)
            print(f"Error during transaction submission: {error_code} ({error_message})")
            return None

        transaction_id = transaction.transaction_id
        print(f"Transaction submitted. Transaction ID: {self._format_transaction_id(transaction_id)}")

        return self._poll_for_receipt(transaction_id, timeout)

    def _submit_transaction_with_retry(self, transaction_proto, submit_method, max_retries=3):
        """Helper method to submit a transaction with retries in case of a 'BUSY' node."""
        for attempt in range(max_retries):
            response = submit_method(transaction_proto)
            if response.nodeTransactionPrecheckCode == response_code_pb2.ResponseCodeEnum.BUSY:
                print(f"Node is busy (attempt {attempt + 1}/{max_retries}), retrying...")
                self.network.select_node()  # switch to a new node
                # update the channel and stubs to use the new node
                self.channel = grpc.insecure_channel(self.network.node_address)
                self.token_stub = token_service_pb2_grpc.TokenServiceStub(self.channel)
                self.crypto_stub = crypto_service_pb2_grpc.CryptoServiceStub(self.channel)
                time.sleep(2)  # wait before retrying
            else:
                return response
        return response

    def _poll_for_receipt(self, transaction_id, timeout):
        """Helper method to poll for transaction receipt within the specified timeout."""
        start_time = time.time()
        receipt = None

        while time.time() - start_time < timeout:
            try:
                receipt = self.network.get_transaction_receipt(transaction_id)
                if receipt:
                    break
            except Exception as e:
                print(f"Error fetching receipt: {e}")
            time.sleep(1)

        if receipt:
            if hasattr(receipt, 'token_id') and receipt.token_id:
                print(f"Created Token ID: {receipt.token_id}")
            return receipt
        else:
            print("Failed to fetch transaction receipt within the timeout period.")
            return None

    def _format_transaction_id(self, transaction_id):
        account_id = transaction_id.accountID
        valid_start = transaction_id.transactionValidStart
        return f"{account_id.shardNum}.{account_id.realmNum}.{account_id.accountNum}-{valid_start.seconds}.{valid_start.nanos}"