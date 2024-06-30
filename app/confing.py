import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("MAIL_HOST")
PORT = int(os.getenv("MAIL_PORT"))
USERNAME = os.getenv("MAIL_USERNAME")
PASSWORD = os.getenv("MAIL_PASSWORD")

from pydantic import BaseModel
from typing import List

class MailBody(BaseModel):
    email: str
    subject: str
    message: str