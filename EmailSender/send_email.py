import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to emails.txt
emails_file = os.path.join(script_dir, 'emails.txt')

try:
    with open(emails_file, 'r') as file:
        to_emails = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print(f'Error: File {emails_file} not found.')
    to_emails = []

def send_email(to_emails: list, subject: str, body: str, image: str | None = None):
    host: str = 'smtp.gmail.com'
    port: int = 465  # Gmail SMTP port for SSL

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print('Logging in...')
        server.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

        for to_email in to_emails:
            # Prepare the email
            print(f'Attempting to send an email to {to_email}')
            message = MIMEMultipart()
            message['From'] = os.getenv('EMAIL')
            message['To'] = to_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            if image:
                # If you have an image attachment function, you can attach it here
                pass

            server.sendmail(os.getenv('EMAIL'), to_email, message.as_string())

            # Success
            print(f'Email sent successfully to {to_email}.')

if __name__ == '__main__':
    if to_emails:
        send_email(to_emails=to_emails, subject='Hey there!!', body='Hello there')
    else:
        print('No recipients found. Exiting.')
