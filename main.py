from datetime import datetime
import smtplib
import pandas as pd
import random

MY_EMAIL = "aditi.shofficial.02@gmail.com"
MY_PASSWORD = "@aditisa24"

today = datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv('birthdays.csv')
# Use dictionary comprehension to create a dictionary from birthday.csv
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthdays_dict:
    # pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with
    # the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the letter generated to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )




