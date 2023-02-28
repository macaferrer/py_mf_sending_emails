from email.message import EmailMessage
import ssl
import smtplib
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email_sender = 'pymacaferrer@gmail.com'
email_password = 'okfhdrdakvvyejmr'
email_receiver = 'macaferrer@gmail.com'
subject = 'check out my new video'
body = html.substitute({'name' : 'Tintin'})

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body, 'html')


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
