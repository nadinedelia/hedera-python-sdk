import os
from dotenv import load_dotenv
from sdk.client.client import Client
from sdk.account.account_id import AccountId
from sdk.crypto.private_key import PrivateKey
from sdk.token.token_create_transaction import TokenCreateTransaction
from sdk.client.network import Network

def main():
    load_dotenv()
    operator_id_str = os.getenv('OPERATOR_ID')
    operator_key_str = os.getenv('OPERATOR_KEY')
    
    if operator_id_str and operator_key_str:
        print("Loading operator credentials from .env file.")
        try:
            operator_id = AccountId.from_string(operator_id_str)
            operator_key = PrivateKey.from_string(operator_key_str)
        except Exception as e:
            print(f"Error parsing operator credentials from .env: {e}")
            return
    else:
        print("Operator credentials not found in .env file.")
        return
        
    # Initialize client
    network = Network()
    client = Client(network)
    client.set_operator(operator_id, operator_key)
    
    # Create TokenCreateTransaction
    token_tx = TokenCreateTransaction()
    token_tx.token_name = "MyToken"
    token_tx.token_symbol = "MTK"
    token_tx.decimals = 2
    token_tx.initial_supply = 1
    token_tx.treasury_account_id = operator_id
    token_tx.transaction_fee = 10_000_000_000  
    
    # Execute transaction
    receipt = client.execute_transaction(token_tx)
    
    if receipt:
        print(receipt)
    else:
        print("\nTransaction failed or receipt not available.")

if __name__ == "__main__":
    main()
