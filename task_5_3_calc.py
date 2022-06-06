# калькулятор с циклами

def addition(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    if b == 0:
        print("Devision by zero. Try again.")
        return a
    else:
        return a/b


var_1 = int(input("Enter first number: "))
result = var_1

while True:
    operation = input("Enter operation +, -, *, / , = : ")
    if operation != "=":
        var_2 = int(input("Enter next number: "))
        if operation == "+":
            result = addition(result, var_2)
            print(result)
        elif operation == "-":
            result = subtraction(result, var_2)
            print(result)
        elif operation == "*":
            result = multiplication(result, var_2)
            print(result)
        elif operation == "/":
            result = division(result, var_2)
            print(result)
        else:
            print("Wrong operator")
    else:
        print("Result = ", result)
        break
