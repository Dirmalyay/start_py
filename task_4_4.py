# Рисуем прямоугольник

a = int(input("Enter height:"))
b = int(input("Enter width:"))

for i in range(0, a):
    for j in range(0, b):
        print("*", end="")
    print()
