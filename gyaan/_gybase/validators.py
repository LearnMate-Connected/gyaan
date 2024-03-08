import re
import datetime

class Validators:
    
    @staticmethod
    def int_validator(val):
        valid = False
        int_val = 0
        try:
            int_val = int(val)
            valid = True
        except:
            pass
        return int_val, valid
    
    @staticmethod
    def float_validator(val):
        valid = False
        float_val = 0
        try:
            float_val = float(val)
            valid = True
        except:
            pass
        return float_val, valid
    
    @staticmethod
    def string_validator(string):
        valid = False
        string_val = ""
        try:
            string_val = float(val)
            valid = True
        except:
            pass
        return string_val, valid
    
    @staticmethod
    def email_validator(email):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        valid  = re.fullmatch(email_regex, email)
        if valid:
            return True
        return False
    
    @staticmethod
    def phone_validator(phone):
        phone_regex = re.compile("^\d{10}$")
        valid = phone_regex.match(phone)
        if valid:
            return True
        return False
    
    
    
    
            