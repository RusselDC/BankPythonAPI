from data_layer.card_transaction_history_dao import CardTransactionHistoryDao
from datetime import datetime

class CardTransactionHistoryBll:
    
    def __init__(self):
        self.__card_transaction_history = CardTransactionHistoryDao()
        
        
    def get_user_history(self, card_number) -> list:
        transact_records = self.__card_transaction_history.get_transactions().get("card_transaction_history")
        
        transact_array = []
        
        for record in list(transact_records):
            if str(card_number) == record.get("account_number"):
                transact_array.append(record)
                
        return transact_array
    
    def save_transaction(self, account_number:int, amount:float, receiver_or_sender: str, description:str, balance:str, mode:str) -> dict:
        transaction_details = {
            "account_number": str(account_number),
            "amount_transacted": 5000,
            "receiver_or_sender": receiver_or_sender,
            "transaction_type": mode,
            "transaction_date": datetime.today().strftime('%Y-%m-%d'),
            "description": description,
            "balance": balance
        }
        
        return self.__card_transaction_history.save_transaction(self.get_transact_id(account_number), transaction_details)
        
    def get_transact_id(self, account_number:int) -> str:
        now = datetime.now()
        msec = now.microsecond
        return f"{account_number}-{now.strftime('%Y%m%d%H%M%S')}{msec:03d}"