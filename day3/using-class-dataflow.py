import requests
import csv
import json
import time 

class UserDataProcessor:
    def __init__(self):
        self.my_url = "https://jsonplaceholder.typicode.com/posts/"

    def fetch_user_data(self,user_id):
        my_para = {
            "userId" : user_id
        }
        response = requests.get(self.my_url , params=my_para , timeout=10)
        response.raise_for_status()
        print(response.status_code)
        return response.json()

    # 2. transformation & validataion 
    def process_data(self,fetched_data):
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
    def export_json(self,data,filename):
        if not data: 
            print("No valid Data found")
            return 
        with open(filename,'w',encoding='utf-8') as f:
            json.dump(data,f,indent=4)
        print(f"json file created : {filename}")

    def main(self):
        user_ID = int(input("Enter user id like (1-10) : "))
        fetch_data = self.fetch_user_data(user_ID)
        transformed_data = self.process_data(fetch_data)

        print("Records data for user ",len(fetch_data))
        print("after validation records are : ",len(transformed_data))
        time.sleep(2)
        print("__"*50)
        print(transformed_data)
        # calling json function 
        self.export_json(transformed_data,"operation_ashu_records3.json")

# execute program 
if __name__ == "__main__" :
    myobj = UserDataProcessor()
    myobj.main()