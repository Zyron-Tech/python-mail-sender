import smtplib
from email.message import EmailMessage
import time

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465  # Using SSL port
SENDER_EMAIL = 'yourmail@gmail.com'  # Replace with your email address
SENDER_PASSWORD = 'Your_Email_Password'  # Replace with your email password or app password

# List of recipients
recipients = [
    'recipient1@gmail.com',
    # Add more emails as needed
]

# Email content
subject = 'This is a Test Email Subject'
body = 'This is the body of the email.'

def send_email(recipient, subject, body, retries=3):
    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient

    attempt = 0
    while attempt < retries:
        try:
            # Using SMTP_SSL for port 465 (SSL)
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
                print(f"Email sent to {recipient}")
                break  # Exit loop if successful
        except Exception as e:
            attempt += 1
            print(f"Failed to send email to {recipient}: {e}")
            if attempt < retries:
                time.sleep(10)  # Wait before retrying

# Send emails to all recipients with a delay between each send
for recipient in recipients:
    send_email(recipient, subject, body)
    time.sleep(5)  # Delay between sending emails to avoid rate limits
