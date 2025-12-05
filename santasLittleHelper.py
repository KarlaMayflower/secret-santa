# Script to send Secret Santa letters to a list of participants
# Santas (txt file) format: name, email

# imports
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

# mail info
elfMail = os.getenv("MAIL_FROM")
northPoleServer = os.getenv("SMTP_SERVER")
northPoleTunnel = os.getenv("SMTP_PORT")
northPoleAccount = os.getenv("ACCOUNT_EMAIL")
magicWord = os.getenv("APP_PASSWORD")

# variables
santasList = [] # recipients
addresses = [] # emails
santas = [] # secret santas
count = 0

# provide Santas
listName = input("Please provide the file name for the list of Santas (must end in .txt): ")

# extract names and emails
with open(listName, "r") as file:
    for line in file:
        name, email = line.strip().split(",")
        santas.append(name)
        addresses.append(email)
        count += 1

# generate random santas
print("Assigning Santas...")
santasList = santas[:]
while any(a == b for a, b in zip(santasList, santas)):
    random.shuffle(santasList)

print("Santas have been assigned!")

# send emails
print("Sending Santa's letters...")
for i in range(count):
    msg = MIMEMultipart()
    msg['From'] = f"Santa's Little Helper <{elfMail}>"
    msg['To'] = addresses[i]
    msg['Subject'] = "Secret Santa"

    body = (
        f"Hi {santas[i]}, \n"
        "\n"
        f"You are the Secret Santa for {santasList[i]}.\n"
        "\n"
        "Happy Holidays!"
    )
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    server = smtplib.SMTP(northPoleServer, northPoleTunnel)
    server.starttls()
    server.login(northPoleAccount, magicWord)
    server.send_message(msg)
    server.quit()

print("Letters have been sent and Santas are ready!\nHappy Holidays!")


        