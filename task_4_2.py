# Вычислить факториал числа

a = int(input("Enter a number to calculate factorial:"))
result = 1

for i in range(1, a+1):
    result = result*i
print("Result:", result)
