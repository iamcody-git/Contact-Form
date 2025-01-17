import smtplib, ssl
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_email(first_name, last_name, user_email, user_message):
    """
    Sends an email with the form data in a standard text format.
    """
    # Email Configuration
    host = "smtp.gmail.com"
    port = 587
    username = os.getenv("EMAIL_USERNAME")  # Load from .env
    password = os.getenv("EMAIL_PASSWORD")  # Load from .env
    receiver = os.getenv("EMAIL_RECEIVER")  # Load from .env

    # Create the email message in plain text format
    subject = "New Contact Form Submission"
    body = f"""
    New Contact Form Submission

    Name: {first_name} {last_name}
    Email: {user_email}
    Message:
    {user_message}
    """

    # Prepare the email headers and content
    message = f"""\
    Subject: {subject}

    {body}
    """

    # Send the email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(host, port) as server:
            server.starttls(context=context)
            server.login(username, password)
            server.sendmail(username, receiver, message.encode("utf-8"))
        return True, "Email sent successfully!"
    except Exception as e:
        return False, f"An error occurred while sending the email: {e}"
