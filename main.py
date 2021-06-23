import pandas as pd

from datetime import date


today_datetime = date.today()
today = str(today_datetime)[5:]

df = pd.read_excel('Birthday_Database.xlsx', sheet_name="Sheet1")
email_list = df[df["Birthday"].astype(str).str[5:] == today].copy()
email_list['Age'] = today_datetime.year - int(email_list['Birthday'].astype(str).str[0:4])

if email_list.empty:
    print("No one to email")
    exit()
else:
    print(email_list)

print("\n\n\n")


