import smtplib
import os

sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_PASSWORD')
receiver_email = os.environ.get('RECEIVER_EMAIL')
receiver_name = os.environ.get('RECEIVER_NAME')

subject = "Generic Title of Email"

message = f"""From: Commemoration Bot 
To: {receiver_name} {receiver_email}
MIME-Version: 1.0
Content-type: text/html
Subject: {subject}

Hello, this is a python bot. Beep Boop!

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Click here to unsubscribe from this email in the future</a>
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email,receiver_email,message)