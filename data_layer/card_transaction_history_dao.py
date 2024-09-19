from data_layer.abstract_json_dao import AbstractJsonDao

class CardTransactionHistoryDao(AbstractJsonDao):
    
    def __init__(self) -> None:
        self.__json_data = self.load_string_from_file()
        
    def get_transactions(self) -> list:
        return list(self.__json_data.get("card_transaction_history").values())

    def save_transaction(self, transaction_id, transaction_details) -> dict:
        json_data = self.__json_data
        json_data.get("card_transaction_history")[transaction_id] = transaction_details
        self._save_file(self._get_file_name(), json_data)
        return json_data.get("card_transaction_history")[transaction_id]
        
    def _get_file_name(self) -> str:
        return "./data/card_transaction_history.json"