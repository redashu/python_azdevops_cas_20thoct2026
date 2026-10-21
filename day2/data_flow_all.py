import requests
import csv
import json
import time 
# Retrive data from API 
def fetch_user_data(user_id):
    my_url = "https://jsonplaceholder.typicode.com/posts/"
    my_para = {
        "userId" : user_id
    }
    response = requests.get(my_url , params=my_para , timeout=10)
    response.raise_for_status()
    print(response.status_code)
    return response.json()


# execute program 
if __name__ == "__main__" :
    fetch_user_data(2)
