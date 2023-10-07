import requests 

# URL for the API 
url = 'http://3.133.140.55:8000/dashboard/update_rack/'



update_data = {
    "vals":{
        "name": "updated from python",
        "status": "good"
    },
    "pk": 4
}

response = requests.post(url,json=update_data)
# response = requests.get(url)
if response.status_code == 200:
    print([response.text,"it's all good man"])
else :
    print(f"Requests failed with status code: {response.status_code}")
        
