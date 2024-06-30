from app.confing import HOST, USERNAME, PASSWORD, PORT, MailBody
from ssl import create_default_context
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from typing import Optional

def send_mail(email: str, subject: str, message: str):
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = SMTP(HOST, PORT)
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, email, msg.as_string())
        server.quit()
        return {"status": 200, "message": "Email has been scheduled"}
    except Exception as e:
        return {"status": 500, "errors": e}
