import json

class FileUtils:
    
    def _open_file(self, file_location:str) -> dict:
        file = open(file_location, 'r')
        opened_file = file.read()
        file.close()
        return opened_file
    
    def _save_file(self, file_location:str, content:str) -> None:
        file = open(file_location, 'w')
        json.dump(content, file, indent=4)
        file.close()
        
        return file