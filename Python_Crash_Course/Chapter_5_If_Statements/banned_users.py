banned_users = ['andrew', 'carolina', 'david']
users = ['marie', 'kyrstin', 'kelli', 'frank', 'david']

for user in users:
    if user not in banned_users:
        print(f"{user.title()}, you can post a response if you wish.")

