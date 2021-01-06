


###ВАРИАНТ 1 - ЧТЕНИЕ
myFile = open("shopping list.txt")
print(myFile.read())
myFile.close()


###ВАРИАНТ 1 - ЗАПИСЬ
myFile = open("shopping list.txt", 'a')
myFile.write("\npotato")
myFile.close()

### ЧТЕНИЕ - 2 варитант(предпочтительный)
with open("shopping list.txt") as myFile:
    print(myFile.read())

###ДОЗАПИСЬ - 2 вариант(предпочтительный)
with open("shopping list.txt", 'a') as myFile:
    print(myFile.read())

