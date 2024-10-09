import grpc
from sdk.outputs import token_service_pb2_grpc
from sdk.token.token_create_transaction import TokenCreateTransaction
from sdk.client.network import Network
from sdk.outputs import timestamp_pb2
from sdk.outputs import basic_types_pb2
from sdk.outputs import response_code_pb2
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

    def set_operator(self, account_id, private_key):
        self.operator_account_id = account_id
        self.operator_private_key = private_key

    def execute_transaction(self, transaction, timeout=60):
        transaction.transaction_id = self._generate_transaction_id()
        transaction.node_account_id = self.network.node_account_id.to_proto()
        transaction.sign(self.operator_private_key)

        transaction_proto = transaction.to_proto()

        if isinstance(transaction, TokenCreateTransaction):
            response = self._submit_transaction_with_retry(transaction_proto)
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


    def _submit_transaction_with_retry(self, transaction_proto, max_retries=3):
        """Helper method to submit a transaction with retries in case of a 'BUSY' node."""
        for attempt in range(max_retries):
            response = self.token_stub.createToken(transaction_proto)
            if response.nodeTransactionPrecheckCode == response_code_pb2.ResponseCodeEnum.BUSY:
                print(f"Node is busy (attempt {attempt + 1}/{max_retries}), retrying...")
                self.network.select_node()  # Switch to a new node
                # Update the channel and stubs to use the new node
                self.channel = grpc.insecure_channel(self.network.node_address)
                self.token_stub = token_service_pb2_grpc.TokenServiceStub(self.channel)
                time.sleep(2)  # Wait before retrying
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
            print(f"Transaction Receipt: Status = {receipt.status}, Cost = {receipt.cost} tinybars")
            if hasattr(receipt, 'token_id') and receipt.token_id:
                print(f"Created Token ID: {receipt.token_id}")
            return receipt
        else:
            print("Failed to fetch transaction receipt within the timeout period.")
            return None

    def _generate_transaction_id(self):
        current_time = timestamp_pb2.Timestamp()
        current_time.seconds = int(time.time())
        current_time.nanos = int((time.time() - current_time.seconds) * 1e9)

        transaction_id = basic_types_pb2.TransactionID()
        transaction_id.accountID.CopyFrom(self.operator_account_id.to_proto())
        transaction_id.transactionValidStart.CopyFrom(current_time)
        transaction_id.scheduled = False
        
        return transaction_id

    def _format_transaction_id(self, transaction_id):
        account_id = transaction_id.accountID
        valid_start = transaction_id.transactionValidStart
        return f"{account_id.shardNum}.{account_id.realmNum}.{account_id.accountNum}-{valid_start.seconds}.{valid_start.nanos}"