# Сумма натуральных чисел в заданном промежутке без рекурсии

def sum_nat(a, b):
    list_ = []
    for i in range(a, b+1):
        list_.append(i)
    return sum(list_)


a1 = int(input("Enter first number: "))
b1 = int(input("Enter second number: "))
print("Sum of numbers is: ", sum_nat(a1, b1))
