# Посчитать количество способов подняться на ступеньку с шагом 1 или 2

def step_(n):
    if n == 1 or n == 2 or n == 3:
        return n
    return step_(n-1)+step_(n-2)


n1 = int(input("Enter quantity of stairs: "))
print("You can do it by", step_(n1), "ways")
