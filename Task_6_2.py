# является ли фраза палиндромом


def palimdrome(pal_str_1):
    pal_str_1 = pal_str.lower()
    ignore_signs = " .,!?:;"
    if pal_str_1 != "":
        pal_str_1 = "".join(i for i in pal_str_1 if i not in ignore_signs)
        pal_str_2 = "".join(reversed(pal_str_1))
        print(pal_str_1)
        print(pal_str_2)
        if pal_str_1 == pal_str_2:
            return print("Palindrome")
        else:
            return print("Not palindrome")
    else:
        print("Empty string")


pal_str = input("Enter the sentence: ")
palimdrome(pal_str)
