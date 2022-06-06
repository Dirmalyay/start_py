# Вывести на экран простые числа. Их сумму или произведение по запросу

def simp_num(b):
    list_ = []
    for i in range(2, b+1):
        for j in list_:
            if i % j == 0:
                break
        else:
            list_.append(i)
    oper = input("Enter + for addition or * for multiplying: ")
    if oper == "+":
        return list_, sum(list_)
    elif oper == "*":
        mult = 1
        for k in list_:
            mult *= k
        return list_, mult
    else:
        print("Wrong operation. List: ", list_)

b1 = int(input("Enter the number to which you want to display sequence: "))
print(simp_num(b1))
