import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()

my_email = "email@gmail.com"
password = "pass"

if weekday == 3:
    with open("./Day32/quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:MONDAY MOTIVATION\n\n{quote}")
        
