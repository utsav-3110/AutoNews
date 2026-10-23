

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

EMAIL_ADDRESS = 'your email'
EMAIL_PASSWORD = 'your password' 





def send_mail(pdf_path):

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS

    mail = input("Enter your mail : ")
    msg["To"] = mail
    msg["Subject"] = "Sending news report throw python"

    body = "This is script run by utsav gangani to send a news latter "
    msg.attach(MIMEText(body, "plain"))


    with open(pdf_path, "rb") as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
        pdf_attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename=os.path.basename(pdf_path)
        )
        msg.attach(pdf_attachment)



    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(" Email sent successfully!")
    except Exception as e:
        print("Error:", e)
