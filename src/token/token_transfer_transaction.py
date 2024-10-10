# src/token_transfer_transaction.py

from src.transaction import Transaction
from src.outputs import crypto_transfer_pb2, transaction_body_pb2
from src.outputs import basic_types_pb2, token_transfer_pb2

class TokenTransferTransaction(Transaction):
    def __init__(self):
        super().__init__()
        self.token_transfers = {} 

    def build_transaction_body(self):
        if not self.token_transfers:
            raise ValueError("Token transfers must be set")

        crypto_transfer_tx_body = crypto_transfer_pb2.CryptoTransferTransactionBody()

        for token_id, transfers in self.token_transfers.items():
            token_transfer_list = token_transfer_pb2.TokenTransferList()
            token_transfer_list.token.CopyFrom(token_id.to_proto())
            for account_id, amount in transfers:
                account_amount = basic_types_pb2.AccountAmount()
                account_amount.accountID.CopyFrom(account_id.to_proto())
                account_amount.amount = amount
                token_transfer_list.transfers.append(account_amount)
            crypto_transfer_tx_body.tokenTransfers.append(token_transfer_list)

        transaction_body = transaction_body_pb2.TransactionBody()
        transaction_body.transactionID.CopyFrom(self.transaction_id)
        transaction_body.nodeAccountID.CopyFrom(self.node_account_id)
        transaction_body.transactionFee = self.transaction_fee
        transaction_body.transactionValidDuration.seconds = self.transaction_valid_duration_seconds
        transaction_body.generateRecord = self.generate_record
        transaction_body.memo = self.memo

        transaction_body.cryptoTransfer.CopyFrom(crypto_transfer_tx_body)

        return transaction_body
