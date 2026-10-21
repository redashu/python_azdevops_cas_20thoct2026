
import requests
import logging

# Configure logging
logging.basicConfig(
    filename="api_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_posts(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        logging.info("Fetching posts for user %s", user_id)

        response = requests.get(
            url,
            params={"userId": user_id},
            timeout=5
        )

        response.raise_for_status()
        posts = response.json()

        if not isinstance(posts, list):
            raise ValueError("Unexpected API response format")

        logging.info("Successfully retrieved %d posts", len(posts))
        print(f"Retrieved {len(posts)} posts")

        return posts

    except requests.exceptions.Timeout:
        logging.error("API request timed out")
        print("Error: Request timed out")

    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error: %s", e)
        print(f"Error: HTTP request failed ({e})")

    except requests.exceptions.RequestException as e:
        logging.error("Network or request error: %s", e)
        print("Error: Unable to reach the API")

    except ValueError as e:
        logging.error("Invalid response data: %s", e)
        print("Error: Invalid response data")

    return []


user_id = input("Enter user ID: ")

if user_id.isdigit():
    posts = get_posts(int(user_id))
    print("Records available:", len(posts))
else:
    logging.warning("Invalid user ID entered")
    print("Please enter a numeric user ID")
