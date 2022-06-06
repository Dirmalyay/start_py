# Создать список, вывести мин., макс., среднее арифм. и сумму значений
def in_list(n):
    list_ = []
    for i in range(n):
        a = int(input("Enter element: "))
        list_.append(a)
    return min(list_), max(list_), sum(list_), sum(list_)/len(list_)


numb = int(input("Enter quantity of numbers: "))
print(in_list(numb))