import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "pythont50@gmail.com"
MY_PASSWORD = "xeecyttyfxgwvixh"
FILE_NAMES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("email_automation/birthdays.csv")
birthday_dict = data.to_dict("records")

for person in birthday_dict:
    if person["month"] == month and person["day"] == day:
        random_letter = random.choice(FILE_NAMES)
        with open(f"email_automation/{random_letter}") as file:
            text = file.read()
            wishes = text.replace("[NAME]", person["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=person["email"], 
                msg=f"Subject: Birthday wishes.\n\n{wishes}"
            )