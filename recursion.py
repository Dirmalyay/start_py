def mult_num(a, b):
    if b == a:
        return b
    while b != a:
        return b * mult_num(a, b - 1)

a1 = int(input("Enter first number: "))
b1 = int(input("Enter second number: "))
print(mult_num(a1, b1))
