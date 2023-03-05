import requests
import json

URL_users = "https://jsonplaceholder.typicode.com/users"

response_users = requests.get(URL_users)
users = json.loads(response_users.text)

URL_posts = "https://jsonplaceholder.typicode.com/posts"

response_posts = requests.get(URL_posts)
posts = json.loads(response_posts.text)

user_id = int(input("Upišite broj (1 - 10) od kojeg korisnika želite ispis podataka i svih njegovih postova: "))
users_dict = {}
i = 1
for user in users:
    if user["id"] == user_id:
        users_dict[user_id] = user
        for post in posts:
            if post["userId"] == user_id:
                users_dict["Posts"][i] = post

# for user in users:
#     try:
#         with open("users.json", "a") as file_writer:
#             file_writer.dump(f"Name: {user['name']}\tAdress: {user['adress']['city']}\n")
#     except Exception as e:
#         print(e)
    
#     for post in posts:
#         try:
#             with open("users.json", "a") as file_writer:
#                 if post["userId"] == user["id"]:
#                     file_writer.dump(f"Post title: {post['title']}")
#         except Exception as e:
#             print(e)
