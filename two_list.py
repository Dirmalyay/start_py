# Выводит уникальные элементы
def uniq_elem(l1, l2):
    list_res = []
    for i in l1:
        for j in l2:
            if i == j:
                list_res.append(j)
            else:
                continue
    return list_res


def uniq_elem_2(l1, l2):
    list_res = []
    for i in l1:
        if i not in l2:
            list_res.append(i)
    for j in l2:
        if j not in l1:
            list_res.append(j)
    return list(set(list_res))


list_1 = ["f", 5, 5, "hh", "p", 9]
list_2 = [2, 3, "f", "hh", "u", 9, "p"]
print(uniq_elem_2(list_1, list_2))
