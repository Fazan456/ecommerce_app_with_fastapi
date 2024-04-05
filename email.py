from fastapi import BackgroundTasks, UploadFile, Form, Depends, HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List
from models import User
import jwt



from dotenv import dotenv_values

config_credentials = dotenv_values('.gitignore')

conf = ConnectionConfig(
    MAIL_USERNAME = config_credentials["EMAIL"]
    MAIL_PASSWORD = config_credentials["PASS"],
    MAIL_FROM = config_credentials["EMAIL"],
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = False,
    MAIL_SSL = True,
    USE_CREDENTIALS = True
)

class EmailSchema(BaseModel):
    email : List[EmailStr]

async def send_email(email: EmailSchema, instance: User):
    token_data {
        "id":instance.id,
        "user_name": instance.username
    }
    token = jwt.encode(token_data, config_credentials["SECRET"])
    



