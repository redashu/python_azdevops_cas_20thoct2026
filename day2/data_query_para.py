import time 
import requests
my_url = "https://jsonplaceholder.typicode.com/posts/"

my_param = {
    "userId" : 1
}
# connect url 
response = requests.get(my_url, params=my_param)

# reading data by converting into json dict

data = response.json()
print(data)
# use for loop 
for i in data: 
    print(f"Title :  {i['title']}")
    print("_"*50)
