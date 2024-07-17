from flask import Flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv


app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
EMAIL_PASS = os.getenv('EMAIL_PASS')
CC_EMAIL = os.getenv('CC_EMAIL')


@app.route('/')
def home():
    return '<a href="http://127.0.0.1:5000/send-email">Send email..!</a>'


@app.route('/send-email')
def send_email():

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Cc'] = CC_EMAIL
    msg['Subject'] = "Python (Selenium) Assignment - Anjesh Kumar"

    # Attach the files
    files = ['confirmation_page.png', 'resume.pdf', 'documentation.pdf']
    for file in files:
        attachment = open(file, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file)}")
        msg.attach(part)

    # Attach the body with the msg instance
    body = ("Please find the attached files.\n\n\n1. Source code:- "
            "https://github.com/r-anjesh/Python-Development/tree/main/Assignment"
            "\n\n2. Related Project:- https://github.com/r-anjesh/Python-Development/blob/main/Day51/main.py")

    msg.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, EMAIL_PASS)
    text = msg.as_string()
    server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL, CC_EMAIL], text)
    server.quit()

    return "Email sent!"


if __name__ == '__main__':
    app.run(debug=True)
