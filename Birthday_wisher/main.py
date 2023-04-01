import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

with open("quotes.txt") as quotes:
    list_quotes = quotes.readlines()
    random_quote = random.choice(list_quotes)

if day_of_week == 0:
    my_email = "@gmail.com"
    password = "enhkhbfkxnwhqvja"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="@yahoo.com",
                            msg= f"Subject: Hello \n\n {random_quote}  ")

