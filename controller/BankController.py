from business_layer.card_information_bll import CardInformationBLL
from business_layer.card_transaction_bll import CardTransactionDaoBLL
from business_layer.card_transaction_history_bll import CardTransactionHistoryBll

class BankController:
    
    def __init__(self) -> None:
        self.__card_info_bll = CardInformationBLL()
        self.__card_transact_bbl = CardTransactionDaoBLL
        self.__card_records_bbl = CardTransactionHistoryBll()
    
    def validate_registration(self, name:str, pin:int,account_number:int) -> list:
        return self.__card_info_bll.validate_registration(name, pin, account_number)
    
    def find_card(self, card_number:int) -> dict:
        return self.__card_info_bll.find_card(card_number)
    
    def deactivate_account(self, card_number:int) -> dict:
        return self.__card_info_bll.deactivate_account(card_number)
    
    def activate_account(self,card_number:int) -> dict:
        return self.__card_info_bll.activate_account(card_number)
    
    def check_pin_code(self, account:dict, pin_code:int) -> bool:
        return self.__card_info_bll.check_pin_code(account, pin_code)
    
    def register_account(self, card_number:int, name:str, pin_code:int) -> bool:
        return self.__card_info_bll.register_card_user(card_number, name, pin_code)
    
    def debit_transact(self, card_number:int, amount:float, receiver_or_sender:str, description:str) -> dict:
        return self.__card_transact_bbl.debit_transaction(card_number, amount, receiver_or_sender, description)
    
    def credit_transact(self, card_number:int, amount:float, receiver_or_sender:str, description:str) -> dict:
        return self.__card_transact_bbl.debit_transaction(card_number, amount, receiver_or_sender, description)
    
    def get_user_history(self, card_number) -> dict:
        return self.__card_records_bbl.get_user_history(card_number)
    
    
