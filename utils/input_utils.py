import re

class InputUtils:
    
    
    def is_valid_string(self, value:any) -> bool:
        pattern = r'^[A-Za-z\s]+$'
        return bool(re.match(pattern, str(value).strip()))
    
    
    def is_float(self, value:any) -> bool:
       try:
           float(value)
           return True
       except:
           return False
       
    def is_int(self, value:any) -> bool:
        try:
            int(value)
            return True
        except:
            return False
        
    def is_not_longer_than(self, value:any, length:int) -> bool:
        return len(str(value)) < length
    
    def is_not_shorter_than(self, value:any, length:int) -> bool:
        return len(str(value)) > length
    
    def length_should_be(self, value:any, length:int) -> bool:
        return len(str(value)) == length
    
    def is_no_less_than(self, value:float, limit:int) -> bool:
        return float(value) > limit
    
    
    def is_not_negative(self, value:any) -> bool:
        return value < 0