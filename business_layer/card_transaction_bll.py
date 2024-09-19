from data_layer.card_transaction_dao import CardTransactionDao
from business_layer.card_transaction_history_bll import CardTransactionHistoryBll
from utils.input_utils import InputUtils
from utils.file_utils import FileUtils
class CardTransactionDaoBLL(InputUtils, FileUtils):
    
    def __init__(self):
        self.__card_transaction_dao = CardTransactionDao()
        self.__card_transaction_bll = CardTransactionHistoryBll
        
    def debit_transaction(self, card_number:int, amount:float, receiver_or_sender:str, description:str) -> dict:
        updated_account_details = self.__card_transaction_dao.debit_transaction(card_number, amount)
        new_balance = updated_account_details.get("card_information").get(str(card_number)).get("balance")
        return self.__card_transaction_bll.save_transaction(card_number, amount, receiver_or_sender, description, new_balance, "debit")
        
    def credit_transaction(self, card_number:int, amount:float, receiver_or_sender:str, description:str) -> dict:
        updated_account_details = self.__card_transaction_dao.credit_transaction(card_number, amount)
        new_balance = updated_account_details.get("card_information").get(str(card_number)).get("balance")
        return self.__card_transaction_bll.save_transaction(card_number, amount, receiver_or_sender, description, new_balance, "credit")
    
    def validate_debit(self, balance:float, amount:float) -> dict:
        return float(balance) >= float(amount)
    
    def validate_transaction(self, card_number:int, amount:float, receiver_or_sender:str, description:str) -> list:
        err_message = []
        
        if not self.is_float(amount):
            err_message.append("Amount must be an valid input Ex: 1500")
        
        if not self.is_int(card_number):
            err_message.append("Card umber must be a valid input. Ex:12312312")
            
        if not self.is_valid_string(receiver_or_sender) or not self.is_valid_string(description):
            err_message.append("Description and Receiver or Sender name must be a character. Ex:Russel Ex:Kumain sa mcdo")
            
        return err_message
            
    def validate_account(self, status:int):
        return int(status) == 1
        
        
        
        