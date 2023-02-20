import requests
import json

URL_users = "https://jsonplaceholder.typicode.com/users"

response_users = requests.get(URL_users)
users = json.loads(response_users.text)

URL_posts = "https://jsonplaceholder.typicode.com/posts"

response_posts = requests.get(URL_posts)
posts = json.loads(response_posts.text)

# user_id = int(input("Upišite ID usera za koje želite ispis postova: "))

# for user in users:
#     if user["id"] == user_id:
#         print(f"{user['name']} naslovi postova su:")
#         for post in posts:
#             if post["userId"] == 1:
#                 print(f"\t{post['title']}")

for user in users:
    try:
        with open("users.json", "a") as file_writer:
            file_writer.write(f"Name: {user['name']}\tAdress: {user['adress']['city']}")
    except Exception as e:
        print(e)
    
    for post in posts:
        try:
            with open("users.json", "a") as file_writer:
                if post["userId"] == user["id"]:
                    file_writer.write(f"Post title: {post['title']}")
        except Exception as e:
            print(e)
