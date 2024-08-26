import pandas as pd
import random 
import datetime as dt
import os
import smtplib as sp
MY_EMAIL = "mh7742462@gmail.com"
MY_PASSWORD = "eugzhymjoidmvssy"

# sp.SMTP(host='localhost', port=587)

folder = "letter_templates"
files_in_folder = os.listdir(folder)

now = dt.datetime.now()
day = now.day
month = now.month

data = pd.read_csv("birthdays.csv") 
for index, row in data.iterrows():
    if row["month"] == month and row["day"] == day:
        letter = random.choice(files_in_folder)
        with open(os.path.join(folder, letter), "r") as f:
            content = f.read()
        new_content = content.replace("[NAME]", row["name"])
        with open(letter, "a") as f:
            f.write(new_content)
        with sp.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row["email"],
                msg=f"Subject: Python Test \n\n{new_content}"
            )

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.