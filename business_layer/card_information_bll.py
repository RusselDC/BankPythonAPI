from data_layer.card_information_dao import CardInformationDao
from utils.input_utils import InputUtils


class CardInformationBLL(CardInformationDao, InputUtils):
    
    def __init__(self):
        self.__card_info_dao = CardInformationDao()
        
    def register_card_user(self, card_number:int, name:str, pin:int) -> dict:
        user_data = {"card_holder" : name.strip(), "status":1, "balance":0,"pin":pin}
        return self.__card_info_dao.register_card_user(card_number,user_data)
    
    def find_card(self, card_number: int) -> dict:
        return self.__card_info_dao.find_card(card_number)

    def activate_account(self, card_number: int) -> dict:
        return self.__card_info_dao.activate_account(card_number)
    
    def deactivate_account(self, card_number: int) -> dict:
        return self.__card_info_dao.deactivate_account(card_number)
    
    def check_pin_code(self, account:dict, pin:int) -> bool:
        return str(account.get("pin")) == str(pin)
    
    def validate_registration(self, name:str, pin:int, card_number:int) -> list:
        err_message = []
        if not self.is_valid_string(name):
            err_message.append("Name must only consist of alphabetical characters and spaces.")
        
        if not self.is_int(pin) or not self.is_int(card_number):
            err_message.append("Pin code and card number must be a number with no decimals. Ex:1111")
            
        return err_message

        