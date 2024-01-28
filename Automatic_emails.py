import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


# Go to the following link :https://myaccount.google.com/apppasswords
#Create an app password, you'll use that password for this code.

# Your credentials
gmail_user = 'xyz@gmail.com'
gmail_app_password = 'pass'  # Use the app password you generated

# Email content
subject = "Your Subject Here"
body = "Your Text here"

# List of emails to send to
email_list = [
    
]

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_app_password)

for email in email_list:
    # Creating the message for each recipient
    message = MIMEMultipart()
    message['From'] = gmail_user
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach the PDF
    filename = 'YourCV.docx'  # Include the full path if the file is not in the same directory


    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(filename)}",
    )
    message.attach(part)

    # Sending the email
    text = message.as_string()
    server.sendmail(gmail_user, email, text)

# Closing the server connection
server.close()

