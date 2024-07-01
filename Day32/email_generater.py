import smtplib

my_email = "email@gmail.com"
password = "your pass"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email , to_addrs="anjesh8877@gmail.com",
    msg="Subject : Hello\n\nHI this is testing mail."
    )
connection.close()