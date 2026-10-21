# importing requred libs

import time 
import requests
# you can use 
# import time,requests

# connecting with URL 

my_url = "https://jsonplaceholder.typicode.com/posts/1"
# connect url 
response = requests.get(my_url)
print(response)
# checking function inside response variable 
print(dir(response))
# reading data in text format 
print("Reading response in Text : ",response.text)
time.sleep(2)
print("http status code : ", response.status_code)
print("checking for URL and json data format ")
print("url orginal : ", response.url)
print("reading json response ")
time.sleep(2)
print("response in json : ",response.json())
