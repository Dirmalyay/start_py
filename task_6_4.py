# Функция вычисляет сумму натуральных чисел, которые входят в заданный промежуток.

def summa(a, b):
    if b == a:
        return b
    else:
        return b + summa(a, b-1)


a1 = int(input("Enter first number: "))
b1 = int(input("Enter second number: "))
print(summa(a1, b1))
