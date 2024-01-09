import smtplib
from email.mime.text import MIMEText
from configparser import ConfigParser

config = ConfigParser()
config.read("settings.ini")

mail_content = config["Conf"]["mail_content"]
subject = config["Conf"]["subject"]
key = config["Conf"]["key"]
my_mail = config["Conf"]["my_mail"]
 
    
class Person:   
    '''
    This class represent each Person that we would like to send email.
    '''
    def __init__(self, name, mail, day, month):
        self.name = name
        self.mail = mail
        self.day = day
        self.month = month

    
    def send_mail(self):
        '''
        This method is called to send email to ceratin person.
        '''
        msg = MIMEText(mail_content)
        msg['Subject'] = subject
        msg['From'] = my_mail
        msg['To'] = self.mail
    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_mail, key)
        server.sendmail(my_mail, self.mail, msg.as_string())
        
        print(f"Mail sended to {self.name}")
        

