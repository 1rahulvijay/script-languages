import imghdr
import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage


def send_mail(to):
    try:
        with open('config.txt', mode='r') as f:
            config = f.read().splitlines()
            print("E-Mail :", config[0], "Password :", config[1])

            time = datetime.now()
            timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
            print(timestamp)

            msg = EmailMessage()
            msg['Subject'] = 'lets go here a for vacation'
            msg['From'] = config[0]
            msg['To'] = to
            msg.set_content('How about next month, are you free ?\n' + timestamp)

            with open('additionalmsg.jpg', 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            print("It will take few seconds \nPlease wait, Additional message to the teacher is uploading")
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(config[0], config[1])

                smtp.send_message(msg)
            print("Mail sent successfully, Have a nice day!")

    except FileNotFoundError:
        print("No file with this name exists")
        sys.exit()


def run():
    send_mail(to=input("Enter your Email ID:  "))


if __name__ == "__main__":
    run()
