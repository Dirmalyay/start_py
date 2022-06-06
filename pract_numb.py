def numb_middle_sum(n):
    numb_list = []
    copy_numb_list = []
    for i in range(n):
        a = int(input("Enter element: "))
        numb_list.append(a)
    numb_list.sort(reverse=True)
    copy_numb_list.extend(numb_list)
    copy_numb_list.sort()
    return numb_list, copy_numb_list, sum(numb_list), sum(numb_list)/len(numb_list)


numb = int(input("Enter quantity of numbers: "))
print(numb_middle_sum(numb))
