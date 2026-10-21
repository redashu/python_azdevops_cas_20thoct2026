import time 
import requests
# connecting with URL 
base_url = "https://jsonplaceholder.typicode.com/posts/"
my_url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(my_url)
print("GET method with http status code : ",response.status_code)
# create new data to send on same URL 
new_data = {
    "userId" : 1,
    "title" : "Casino Operation Report",
    "body" : "Daily operation report summary"
}
# sending data using post method 

reponse_new = requests.post(base_url , json=new_data)
print("POST method code : ",reponse_new.status_code)
print("Created Record : ",reponse_new.json())
