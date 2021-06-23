import smtplib
import os
import pandas as pd
from datetime import date

# An example of the output of date.today() would be 2021-06-22. We only want the 06-22 part
today_datetime = date.today()
today = str(today_datetime)[5:]

email_list = pd.read_excel('Birthday_Database.xlsx', sheet_name="Sheet1")

email_list = email_list[email_list["Birthday"].astype(str).str[5:] == today]

# If there is no one to email today, stop the execution of the program
if email_list.empty:
    exit()

# If the execution reaches beyond this point, there is a natural implication that there are people to email
email_list['Age'] = today_datetime.year - (email_list['Birthday'].astype(str).str[0:4].astype(int))

# # The email and password for the email bot are stored in environment variables
sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_PASSWORD')

# The line directly below is the bottleneck; however, it is essential for the code to work
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

greeter = "Congratulations!"
message_body = "This is a bot created to wish you a happy birthday as I am pretty terrible with remembering myself...."
closing_statement = "Thank you"


for row in email_list.itertuples():
    receiver_name = getattr(row,'Name')
    receiver_email = getattr(row, 'Email')
    subject = f"In commemoration of turning {getattr(row,'Age')} years old!"

    message = f"From: Commemoration Bot\n" \
              f"To: {receiver_name} {receiver_email}\n" \
              f"MIME-Version: 1.0\n" \
              f"Content-type: text/html\n" \
              f"Subject: {subject}\n" \
              f"{greeter}\n" \
              f"<br><br>\n" \
              f"{message_body}\n" \
              f"<br><br>\n" \
              f"{closing_statement},\n" \
              f"<br><br>\n" \
              f"Haris M."

    server.sendmail(sender_email, receiver_email, message)

server.quit()