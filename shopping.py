print("Привет! Это список покупок")

while True:
    answer = input(
        "(1) - Добавить продукт, (2) - Посмотреть список,  (3) - Удалить продукт из списка, (0) - закрыть программу\n>>>")

    if answer == '1':
        item = input("Что добавляем?\t")
        with open("shopping list.txt", 'a') as myFile:
            myFile.write("\n" + item)

    if answer == '2':
        with open("shopping list.txt") as myFile:
            print(myFile.read())

    if answer == '3':
        item = input("Что нужно удалить?")

        with open("shopping list.txt") as myFile:
            # print(type(myFile.read()))
            products = myFile.read().split('\n')
            if item in products:
                print("Есть такой продукт")
                products.remove(item)
            else:
                print('Такого продукта нет')

        with open("shopping list.txt", 'w') as myFile:
            myFile.write('\n'.join(products))

