import time 
import requests
my_url = "https://jsonplaceholder.typicode.com/posts/1"
# connect url 
response = requests.get(my_url)

print("reading json response ")
time.sleep(2)
data = response.json()
print(type(data))
# extracting details from python dictonary 

print("Post ID : ",data['id'])
print("User ID : ",data['userId'])
print("Title  : ",data['title'])

# user for loop 
print(data.keys())
for i in data.keys():
    print("print info ..",data[i])

