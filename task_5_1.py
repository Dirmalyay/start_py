# Функция выводит имя

def name_print(name):
    if name == "":
        print("Hello, Alex!")
    else:
        print("Hello,", name)


name = input("Enter your name: ")
name_print(name)
