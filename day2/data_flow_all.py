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


# 2. transformation & validataion 
def process_data(fetched_data):
    transformed_records = []
    # define some basic transformation 
    for i in fetched_data:
        record = {
            "record_id" : i.get("id"),
            "user_id" : i.get("userId"),
            "title" : i.get("title","").strip().title(),
            "body" : i.get("body","").strip()

        }
    # basic validation 
        if (
            isinstance(record["record_id"], int)
            and isinstance(record["user_id"], int)
            and record["title"]
            and record["body"]
        ):
            transformed_records.append(record)

    return transformed_records

# save data into json file -- export to json 
def export_json(data,filename):
    if not data: 
        print("No valid Data found")
        return 
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=4)
    print(f"json file created : {filename}")

# main workflow calling function here 

def main():
    user_ID = int(input("Enter user id like (1-10) : "))
    fetch_data = fetch_user_data(user_ID)
    transformed_data = process_data(fetch_data)

    print("Records data for user ",len(fetch_data))
    print("after validation records are : ",len(transformed_data))
    time.sleep(2)
    print("__"*50)
    print(transformed_data)
    # calling json function 
    export_json(transformed_data,"operation_ashu_records.json")

# execute program 
if __name__ == "__main__" :
    main()
