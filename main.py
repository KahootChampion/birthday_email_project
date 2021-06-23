import pandas as pd

from datetime import date

today = date.today()
today = str(today)[5:]

df = pd.read_excel('Birthday_Database.xlsx', sheet_name="Sheet1")
email_list = df[df["Birthday"].astype(str).str[5:] == today]



if email_list.empty:
    print("No one to email")
    exit()
else:
    print(email_list)
