from datetime import date
import time
from person import Person
import csv
from validation import *


if __name__ == "__main__":
    all_persons = []
        
    with open('list.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        row_number = 1        
        for row in csv_reader:
            print(f'loading row number: {row_number}')
            month = validate_month(row['month'])
            day = validate_day(row['day'], row['month'])
            mail = validate_mail(row['mail'])
            
            person = Person(name= row['name'], mail= mail, day= day, month= month)
            all_persons.append(person)
            row_number += 1             
            
    while True:  
        today = date.today()
        for person in all_persons:
            if person.day == today.day and person.month == today.month:
                pass
                # person.send_mail()                        
        time.sleep(60*60*24)
        