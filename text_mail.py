import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT =  587

FROM_EMAIL = "shelves-status@outlook.com"
TO_EMIAL = "jatr160397@gmail.com"

PASSWORD = getpass.getpass("Enter password: ")
MESSAGE = """Subject: Mail sent using python
Hi there ,
This is the statuts of all the balance with the last generation equipment

all good

thanks,
test account"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL,PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMIAL, MESSAGE)

smtp.quit()



