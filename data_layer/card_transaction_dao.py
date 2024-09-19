from data_layer.abstract_json_dao import AbstractJsonDao

class CardTransactionDao(AbstractJsonDao):
    
    def __init__(self) -> None:
        self.__json_data = self.load_string_from_file()
        
    def debit_transaction(self, card_number:int, amount:float) -> dict:
        json_data = self.__json_data
        json_data.get("card_information").get(str(card_number))["balance"] -= amount
        self._save_file(self._get_file_name(), json_data)
        return json_data
    
    def credit_transaction(self, card_number:int, amount:float) -> dict:
        json_data = self.__json_data
        json_data.get("card_information").get(str(card_number))["balance"] += amount
        self._save_file(self._get_file_name(), json_data)
        return json_data
        
        
    def _get_file_name(self) -> str:
        return "./data/card_information.json"