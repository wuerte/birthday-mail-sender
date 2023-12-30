from datetime import date
import time
from person import Person


all_persons = []
radek = Person(mail="radocha.w@gmail.com", name="Radek", day=30, month=12)
all_persons.append(radek)
jacek = Person(mail="rad.wierzgala@gmail.com", name="Jacek", day=30, month=12)
all_persons.append(jacek)

if __name__ == "__main__":
    while True:  
        today = date.today()
        for person in all_persons:
            if person.day == today.day and person.month == today.month:
                person.send_mail()
                
                
        time.sleep(3)
        # time.sleep(60*60*24)
        