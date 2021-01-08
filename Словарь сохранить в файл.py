import pickle


# users = {
#     'admin': 1234,
#     'user': 0000,
# }
with open("userPass.txt", 'rb') as myUsersFile:
    users = pickle.load(myUsersFile)

print(type(users))

while True:
    username = input("USERNAME: ")
    if username == "STOP":
        break
    password = int(input("PASS: "))

    if username in users.keys():
        if users[username] == password:
            print(f'Hello, {username}, welcome back')

        if users[username] != password:
            print("Incorrect password")

    else:
        users[username] = password
        print("New user was created")

    print(users)


with open("userPass.txt", 'wb') as myUsersFile:
    pickle.dump(users, myUsersFile )

