from datetime import date
import time
from person import Person
import csv
import validation


if __name__ == "__main__":
    all_persons = []
        
    with open('list.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        row_number = 1        
        for row in csv_reader:
            print(f'loading row number: {row_number}')
            month = validation.validate_month(row['month'])
            day = validation.validate_day(row['day'], row['month'])
            mail = validation.validate_mail(row['mail'])
            
            person = Person(name= row['name'], mail= mail, day= day, month= month)
            all_persons.append(person)
            row_number += 1             
            
    while True:  
        today = date.today()
        for person in all_persons:
            if person.day == today.day and person.month == today.month:
                person.send_mail()                        
        time.sleep(60*60*24)
        