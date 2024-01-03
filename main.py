from datetime import date
import time
from person import Person
import csv


if __name__ == "__main__":
    all_persons = []
    
    with open('list.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)        
        for row in csv_reader:
            person = Person(name= row['name'], mail= row['mail'], day= int(row['day']), month= int(row['month']))
            all_persons.append(person)             
            
    while True:  
        today = date.today()
        for person in all_persons:
            if person.day == today.day and person.month == today.month:
                person.send_mail()                        
        time.sleep(60*60*24)
        