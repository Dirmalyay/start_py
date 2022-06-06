# Создайте список, введите количество его элементов и сами значения, выведите эти значения на экран в обратном порядке.

def rev_list(num):
    list_new = []
    for i in range(num):
        a = input("Enter element value: ")
        list_new.append(a)
    return list_new[::-1]


num = int(input("Enter quantity of elements in list: "))
print(rev_list(num))
