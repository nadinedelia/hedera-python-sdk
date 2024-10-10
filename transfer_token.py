# transfer_token.py

import os
from dotenv import load_dotenv
from src.client.client import Client
from src.account.account_id import AccountId
from src.token.token_id import TokenId
from src.crypto.private_key import PrivateKey
from src.token.token_transfer_transaction import TokenTransferTransaction
from src.client.network import Network

def main():
    load_dotenv()
    operator_id_str = os.getenv('OPERATOR_ID')
    operator_key_str = os.getenv('OPERATOR_KEY')
    recipient_id_str = os.getenv('RECIPIENT_ID')
    token_id_str = os.getenv('TOKEN_ID')

    if operator_id_str and operator_key_str and recipient_id_str and token_id_str:
        print("Loading credentials from .env file.")
        try:
            operator_id = AccountId.from_string(operator_id_str)
            operator_key = PrivateKey.from_string(operator_key_str)
            recipient_id = AccountId.from_string(recipient_id_str)
            token_id = TokenId.from_string(token_id_str)
        except Exception as e:
            print(f"Error parsing credentials from .env: {e}")
            return
    else:
        print("Credentials or TOKEN_ID not found in .env file.")
        return

    # Initialize client
    network = Network()
    client = Client(network)
    client.set_operator(operator_id, operator_key)

    # Create TokenTransferTransaction
    transfer_tx = TokenTransferTransaction()
    transfer_tx.token_transfers = {
        token_id: [
            (operator_id, -10),  # Deduct 10 tokens from operator's account
            (recipient_id, 10)   # Add 10 tokens to recipient's account
        ]
    }
    transfer_tx.transaction_fee = 10_000_000  # Adjust as needed

    # Execute transaction
    receipt = client.execute_transaction(transfer_tx)

    if receipt:
        print("Token transfer successful.")
        print(receipt)
    else:
        print("\nToken transfer failed or receipt not available.")

if __name__ == "__main__":
    main()
