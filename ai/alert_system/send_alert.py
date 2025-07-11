import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_email_alert(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = os.getenv("SENDER_EMAIL")
    msg["To"] = to_email
    
    # Retrieve sender email and app password from environment variables
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")
    
    if not sender_email or not app_password:
        print("Sender email or app password is missing. Please set them in the .env file.")
        return

    # Sending the email via Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        try:
            # Log in to your Gmail account with the app password
            smtp.login(sender_email, app_password)
            
            # Send the email message
            smtp.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
