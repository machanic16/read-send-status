import RPi.GPIO as GPIO
from hx711 import HX711
import getpass
import smtplib


GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6,
        pd_sck_pin=5
        )

hx.zero()
input('Place know weigt on scale & press Enter:')
reading = hx.get_data_mean(readings=100)

known_weight_grams = input('Enter the know weight in grams & press Enter: ')
value = float(known_weight_grams)

ratio = reading/value

hx.set_scale_ratio(ratio)


while True:
#    data = hx.get_raw_data_mean()
    weight = hx.get_weight_mean()
    print(weight)
    
    if weight <250:
        print('Low inventory')

        HOST = "smtp-mail.outlook.com"
        PORT =  587

        FROM_EMAIL = "shelves-status@outlook.com"
        TO_EMIAL = "jatr160397@gmail.com"

        PASSWORD = getpass.getpass("Enter password: ")
        MESSAGE = """Subject: Mail sent using python
Hi there ,
This is the status of all the balance with the last generation equipment

the weight of total inventory is """ + str(weight) + "g  " + """

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


