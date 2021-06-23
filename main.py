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

if email_list.empty:
    print("No one to email")
    exit()
else:
    email_list['Age'] = today_datetime.year - (email_list['Birthday'].astype(str).str[0:4].astype(int))
    #print(email_list)

# If the execution reaches beyond this point, there is a natural implication that there are people to email

for index, row in email_list.iterrows():
    print(f"{row['Name']} {row['Email']}")

print("\n\n\n")


