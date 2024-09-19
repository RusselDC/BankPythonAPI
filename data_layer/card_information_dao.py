from data_layer.abstract_json_dao import AbstractJsonDao

class CardInformationDao(AbstractJsonDao):
    
    def __init__(self) -> None:
        self.__json_data = self.load_string_from_file()
        
    def get_card_accounts(self) -> dict:
        return self.__json_data
    
    def find_card(self, card_number:int) -> dict:
        return self.__json_data.get("card_information", None).get(str(card_number), None)
    
    def register_card_user(self,card_number:int, user_information:dict) -> dict:
        json_data = self.__json_data
        json_data.get("card_information")[str(card_number)] = dict(user_information)
        self._save_file(self._get_file_name(), json_data)
        return json_data.get("card_information")[str(card_number)]
    
    def deactivate_account(self, card_number:int) -> dict:
        json_data = self.__json_data
        json_data.get("card_information").get(str(card_number))["status"] = 0
        self._save_file(self._get_file_name(), json_data)
        return json_data.get("card_information").get(str(card_number))
    
    def activate_account(self, card_number:int) -> dict:
        json_data = self.__json_data
        json_data.get("card_information").get(str(card_number))["status"] = 1
        self._save_file(self._get_file_name(), json_data)
        return json_data.get("card_information").get(str(card_number))
        
    
    def _get_file_name(self) -> str:
        return "./data/card_information.json"