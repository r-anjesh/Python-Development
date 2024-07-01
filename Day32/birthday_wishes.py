##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import smtplib
import random


my_email = "email@gmail.com"
password = "your pass"


now = dt.datetime.now()
current_month = now.month
current_date = now.day
# print(current_date, current_month)


letter_file = open(f"./day32/letter_templates/letter_{random.randint(1,3)}.txt")
letter_text = letter_file.read()

#  Replacing text in letter
def mail_text():
    letter_to_send = letter_text.replace('[NAME]', birthday['name'])
    return letter_to_send.title()

df = pandas.read_csv("./day32/birthdays.csv")
birthdays_list = df.to_dict(orient="records")
for birthday in birthdays_list:
    if birthday['month'] == current_month and birthday['day'] == current_date:
        with smtplib.SMTP("smtp.gmail.com", port= 587)  as connection:
            connection.starttls()
            connection.login(user=my_email, password= password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday['email'],
                msg=f'Subject: HAPPY BIRTHDAY\n\n{mail_text()}'
                )