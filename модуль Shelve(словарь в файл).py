import shelve


users = shelve.open("MyUsers.db")

users['admin'] = 1234
users['user'] = 0000

print(type(users))
print(users['admin'])

while True:
    username = input("USERNAME: ")
    if username == "STOP":
        break
    password = int(input("PASS: "))
    if password == 0:
        oldPass, newPass = input("Enter old pass and new pass").split()

        if int(oldPass) == users[username]:
            users[username] = int(newPass)
            print("Pass changed")
        else:
            print("incorrect pass")

    if username in users.keys():
        if users[username] == password:
            print(f'Hello, {username}, welcome back')

        if users[username] != password:
            print("Incorrect password")

    else:
        users[username] = password
        print("New user was created")

    print(*users)



