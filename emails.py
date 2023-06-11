import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a multipart message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    # Start the SMTP session and login
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)

    # Close the SMTP session
    server.quit()

# Example usage
sender_email = 'jatr160397@gmail.com'
sender_password = 'Bmxeselmejordeporte'
recipient_email = 'jtovar.fsaeuse@gmail.com'
subject = 'Hello from Python!'
message = 'This is the body of the email.'

send_email(sender_email, sender_password, recipient_email, subject, message)
