import smtplib
from email.mime.text import MIMEText

mail_content = """
        Hello,
        Today is Your birthsday
    """
subject = "test title"
key = "dbjztgprpebwissj" 
my_mail = "rad.wierzgala@gmail.com"
# text = f"Subjetct: {subject} \n\n {mail_content}"
    
class Person:   
    def __init__(self, name, mail, day, month):
        self.name = name
        self.mail = mail
        self.day = day
        self.month = month

    
    def send_mail(self):
        msg = MIMEText(mail_content)
        msg['Subject'] = subject
        msg['From'] = my_mail
        msg['To'] = self.mail
    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_mail, key)
        server.sendmail(my_mail, self.mail, msg.as_string())
        
        print(f"Mail sended to {self.name}")
        

