from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import EmailStr, BaseModel
import app.config as con


class EmailSchema(BaseModel):
    email: EmailStr

conf = ConnectionConfig(
   MAIL_USERNAME=con.MAIL_USERNAME,
   MAIL_PASSWORD=con.MAIL_PASSWORD,
   MAIL_FROM=con.MAIL_FROM,
   MAIL_PORT=con.MAIL_PORT,
   MAIL_SERVER=con.MAIL_SERVER,
   MAIL_STARTTLS=con.MAIL_TLS,
   MAIL_SSL_TLS=con.MAIL_SSL,
   USE_CREDENTIALS=True
)


fm = FastMail(conf)


async def send_email(to_email:EmailSchema, otp: str):
    
    subject = "Password Reset OTP"
    body = f"""
    <h3>Your OTP for password reset is:</h3>
    <h1>{otp}</h1>
    <p>This OTP is valid for 5 minutes. Please do not share it with anyone.</p>
    """

    message = MessageSchema(
        subject=subject,
        recipients=[to_email],
        body=body,
        subtype="html"
    )
    # print("email sent!!!", message)

    await fm.send_message(message)
