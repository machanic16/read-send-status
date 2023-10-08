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

weight_to_measure = 1000


while True:
#    data = hx.get_raw_data_mean()
    weight = hx.get_weight_mean()
    print(weight)
    
    if weight > weight_to_measure*0.85 :
        print('full inventory')

        update_data= {
                "vals": { 
                    "name": "9Y",
                    "status" : "full"
                    },
                "pk":4
                }

        response = requests.post(url,json=update_data)
        if response.status_code == 200:
            print([response.text,"it's all good man"])
        else :
            print(f"Requests failed with status code: {response.status_code}")
        continue

    if weight > weight_to_measure*0.65 :
        print('Good level of inventory')
        update_data= {
                "vals": { 
                    "name": "9Y",
                    "status" : "good"
                    },
                "pk":4
                }         

        response = requests.post(url,json=update_data)
        if response.status_code == 200:
            print([response.text,"it's all good man"])
        else :
            print(f"Requests failed with status code: {response.status_code}")
        continue


    if weight > weight_to_measure*0.40:
        print('needs to be checked')
        update_data= {
                "vals": { 
                    "name": "9Y",
                    "status" : "needs_refill"
                    },
                "pk":4
                }         

        response = requests.post(url,json=update_data)
        if response.status_code == 200:
            print([response.text,"it's all good man"])
        else :
            print(f"Requests failed with status code: {response.status_code}")
        continue

    print('empty')
    update_data= {
                "vals": { 
                    "name": "9Y",
                    "status" : "empty"
                    },
                "pk":4
                }         

    response = requests.post(url,json=update_data)
    if response.status_code == 200:
        print([response.text,"it's all good man"])
    else :
        print(f"Requests failed with status code: {response.status_code}")
    
   

