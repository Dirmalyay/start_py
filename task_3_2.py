# Вычисление функции у для х в диапазоне от -10 до 10 с шагом 1.

x = int(input("Enter value x:"))
y = None

if -5 <= x <= 5:
    y = x**2
elif -10 <= x < -5:
    y = abs(x)*2-1
elif 5 < x <= 10:
    y = 2*x
else:
    print("Error. Enter x value between -10 and 10.")
print("y=", y)
