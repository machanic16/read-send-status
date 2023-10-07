import RPi.GPIO as GPIO
from hx711 import HX711
import getpass
#import smtplib
import requests 
import os

# URL for the API 
url = 'http://3.133.140.55:8000/dashboard/update_rack/'


GPIO.setmode(GPIO.BCM)

hx = HX711(dout_pin=6,
        pd_sck_pin=5
        )

hx.zero()
#input('Place know weigt on scale & press Enter:')
#reading = hx.get_data_mean(readings=100)

#known_weight_grams = input('Enter the know weight in grams & press Enter: ')
#value = float(known_weight_grams)

#ratio = reading/value

ratio = 24.96 # this was calculated with the commented line above

hx.set_scale_ratio(ratio)

treshold_weight = 250


while True:
#    data = hx.get_raw_data_mean()
    weight = hx.get_weight_mean()
    print(weight)
    
    if weight < treshold_weight:
        print('Low inventory')

        data= {
                "vals": { 
                    "name": "Updated from Rasberry PI",
                    "status" : "needs_refill"
                    },
                "pk":4
                }

        response = requests.post(url,data)
        if response.status_code == 200:
            print([response.text,"it's all good man"])
        else :
            print(f"Requests failed with status code: {response.status_code}")
    else:
        print('Good level of inventory')
        data= {
                "vals": { 
                    "name": "Updated from Rasberry PI-",
                    "status" : "good"
                    },
                "pk":4
                }         

        response = requests.post(url,data)
        if response.status_code == 200:
            print([response.text,"it's all good man"])
        else :
            print(f"Requests failed with status code: {response.status_code}")



