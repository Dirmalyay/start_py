# Вывести сумму всех натуральных чисел

a = int(input("Enter first number of sequence:"))
b = int(input("Enter last number of sequence:"))
result = 0

for i in range(a, b+1, 1):
    result += i
print("The sum of sequence:", result)
