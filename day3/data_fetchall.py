import requests
import json
import time


# 1. Retrieve data from API
def fetch_user_data(user_id):
    my_url = "https://jsonplaceholder.typicode.com/posts/"
    my_para = {"userId": user_id}

    response = requests.get(
        my_url,
        params=my_para,
        timeout=10
    )
    response.raise_for_status()

    print(response.status_code)
    return response.json()


# 2. Transform and validate data
def process_data(fetched_data):
    transformed_records = []

    for i in fetched_data:
        record = {
            "record_id": i.get("id"),
            "user_id": i.get("userId"),
            "title": i.get("title", "").strip().title(),
            "body": i.get("body", "").strip()
        }

        if (
            isinstance(record["record_id"], int)
            and isinstance(record["user_id"], int)
            and record["title"]
            and record["body"]
        ):
            transformed_records.append(record)

    return transformed_records


# 3. Export data to JSON
def export_json(data, filename):
    if not data:
        print("No valid Data found")
        return

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"json file created: {filename}")


# 4. Main workflow
def main():
    #user_id = int(input("Enter user id (1-10): "))

    fetched_data = fetch_user_data(5)
    transformed_data = process_data(fetched_data)

    print("Records retrieved:", len(fetched_data))
    print("Records after validation:", len(transformed_data))

    time.sleep(2)
    print("__" * 50)
    print(transformed_data)

    export_json(
        transformed_data,
        "operation_ashu_records.json"
    )


if __name__ == "__main__":
    main()
