import requests

# responses1 = requests.get("https://api.github.com") 

# print(responses1.status_code)
# print(responses1.json())


# responses2 = requests.get("https://api.github.com/users/Torvalds") 

# data = responses2.json()

# print(data)
# print(data["name"])
# print(data["followers"])
# print(data["public_repos"])
# print(data["company"])
# print(data["blog"])

username = input("Enter username for your github profile : ")
response3 = requests.get(f"https://api.github.com/users/{username}")
data = response3.json()
if response3.status_code == 200:
    print(f"Name : {data['name']}")
    print(f"Followers : {data['followers']}")
    print(f"Following : {data['following']}")
    print(f"Public repositories : {data['public_repos']}")
    print(f"Location : {data['location']}")
    print(f"Company : {data['company']}")
    print(f"Blogs : {data['blog']}")
    print(f"Account Created At: {data['created_at']}")
else:
    print("User not found")