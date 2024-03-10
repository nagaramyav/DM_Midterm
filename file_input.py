import pandas as pd
import os
from select_database import select_database

def read_transactions_from_file(file_path):
    transactions = pd.read_csv(file_path, header=None)
    #print("Transactions: ", transactions)
    return transactions

if __name__ == "__main__":
    selected_database = select_database()
    if selected_database:
        print(f"Selected database: {selected_database}")
        
        file_path = os.path.join(os.getcwd(), selected_database)
        transactions = read_transactions_from_file(file_path)
        print("Transactions read from file:")
        print(transactions)
