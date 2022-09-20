# ----------------- Send Emails with Python ---------------- #
import smtplib

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

# connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs="appbrewerytesting@yahoo.com", 
        msg="Subject: Hello\n\nThis is the body of my email."
    )
# connection.close()


# -----------Workin with date and time in Python ------------ #
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
day_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(day_of_birth)


# ------------- Monday Motivation Challenge ----------------- #
import random
import datetime as dt
import smtplib

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )