#Birthday Email Project

Oftentimes, we feel guilty when we forget the birthdays of those close to us. It would be useful to have some sort of tool which automatically wishes our loved ones happy birthday on that special day. This is is why I started developing this project.

## How it Works

When birthday_email.py is executed, it analyzes an Excel file titled "Birthday_Database.xslx". This Excel spreadsheet contains information about those you wish to automatically send birthday wishes to. The code analyzes the spreadsheet and determines if it should send those listed in the spreadsheet a happy birthday message. This code is meant to be run once daily preferably with the use of some sort of task scheduler.

##Prerequisites

### Excel Spreadsheet

The code itself relies on being provided with an excel spreadsheet titled "Birthday_Database.xslx". The spreadsheet must be formatted to have three headers: Name, Birthday, and Email. The birthday should be formatted in the form xxxx-xx-xx where first comes the year, then the month, then the day.

### Task Scheduler

Linux and Mac operating systems often come equipped with a function known as the "crontab". The crontab can be used to run a specific program automatically on a set time and day, in fact, there is so much freedom that a user can specify if the task should repeat daily, monthly, weekly, or annually. The crontab commands can be customized to run as often or as rarely as the user would like. In order to make the most out of this project, I would recommend the use of a crontab which runs daily. Attached in this project is an example fo a crontab command one could utilize. What about those who have a Windows based operating system? Fear not. Windows has a similiar functionality to the crontab which it offers known as the "Task Scheduler". For those on Mac specifically, there is one more option called the "launchd" command. This command is similar to the crontab; however, even if your device is asleep when the task is scheduled, the program will execute when the device wakes up.  