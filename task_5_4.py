# Вычисление среднего арифметического 3х чисел
def middle(a, b, c):
    return (a+b+c)/3


_exit_ = 1
while _exit_ == 1:
    a1 = float(input("Enter first number: "))
    b1 = float(input("Enter second number: "))
    c1 = float(input("Enter thread number: "))
    print("Average: ", middle(a1, b1, c1))
    _exit_ = input("Press 0 to exit, continue - Enter ")
    if _exit_ == 0:
        break
