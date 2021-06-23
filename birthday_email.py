import smtplib
import os

sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_PASSWORD')


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

receiver_email = os.environ.get('RECEIVER_EMAIL')
receiver_name = os.environ.get('RECEIVER_NAME')

subject = "In commemoration of turning 20 years old!"
greeter = "Congratulations!"
message_body = "This is a bot created to wish you a happy birthday as I am pretty terrible with remembering myself...."
closing_statement = "Thank you"

message = f"""From: Commemoration Bot 
To: {receiver_name} {receiver_email}
MIME-Version: 1.0
Content-type: text/html
Subject: {subject}
{greeter}
<br>
<br>
{message_body}
<br>
<br>
{closing_statement},
<br>
<br>
Haris M.
"""

server.sendmail(sender_email,receiver_email,message)