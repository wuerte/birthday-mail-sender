import re

def validate_month(month):
    try:
        val = int(month)
    except:
        raise ValueError("Month must be integer!")
    if isinstance(val, int) and (1 <= val <= 12):
        return int(val)
    else:
        raise ValueError("Month must be in range from 1 to 12!")

  
def validate_day(day, month):
    month_dict = {"1": 31, "2": 29, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31, "9": 30, "10": 31, "11":30, "12": 31}
    try:
        val = int(day)
    except ValueError:
        raise Exception("Day must be integer!")      
    if isinstance(val, int) and (1 <= val <= month_dict[str(month)]):
        return int(val)
    else:
        raise Exception("Day must be in range from 1 to lenght of ceratin month!")
    

def validate_mail(mail):  
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
    if(re.fullmatch(regex, mail)):
        return mail
    else:
        raise Exception("Invalid Email")