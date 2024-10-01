from email.message import EmailMessage
from emailsend import password
import ssl
import smtplib


email_sender = 'asasas15919@gmail.com'
email_password = password

email_receiver = 'refefor709@abevw.com'

subject = "my 1st email sender "
body = """
My name is Aafrith
"""

em = EmailMessage()
em['From'] = email_sender

em['To'] = email_receiver

em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
    print("Email sent successfully")