from abc import ABC
from utils.file_utils import FileUtils
import json

class AbstractJsonDao(ABC, FileUtils):
    def load_string_from_file(self) -> dict:
        print(self._get_file_name())
        return json.loads(self._open_file(self._get_file_name()))
    
    def _get_file_name(self) -> str:
        pass