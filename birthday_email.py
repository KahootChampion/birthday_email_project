import smtplib
import os
import pandas as pd
from datetime import date

# An example of the output of date.today() would be 2021-06-22. We only want the 06-22 part
today_datetime = date.today()
today = str(today_datetime)[5:]

df = pd.read_excel('Birthday_Database.xlsx', sheet_name="Sheet1")

# email_list must be a copy of the original data frame to make pandas aware that any changes to email_list should not
# be applied to the original dataframe. If a copy was not made, when we add an "age" column later on,
# a SystemCopyError would be thrown

email_list = df[df["Birthday"].astype(str).str[5:] == today].copy()

# If there is no one to email today, stop the execution of the program
if email_list.empty:
    exit()

# If the execution reaches beyond this point, there is a natural implication that there are people to email
email_list['Age'] = today_datetime.year - (email_list['Birthday'].astype(str).str[0:4].astype(int))

# The email and password for the email bot are stored in environment variables
sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_PASSWORD')


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

greeter = "Congratulations!"
message_body = "This is a bot created to wish you a happy birthday as I am pretty terrible with remembering myself...."
closing_statement = "Thank you"


for index, row in email_list.iterrows():
    receiver_name = row['Name']
    receiver_email = row['Email']
    subject = f"In commemoration of turning {row['Age']} years old!"

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

    server.sendmail(sender_email, receiver_email, message)

