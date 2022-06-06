# Две функции, вычисляющие значения выражений с шагом 0,5

def funk_1(b):
    return 2+b


def funk_2(b):
    return 2*b


i = -5
while i < 6:
    print('|{:^ 10.1f}|{:^ 10.1f}|'.format(funk_1(i), funk_2(i)))
    i += 0.5
