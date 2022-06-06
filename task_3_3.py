# Решение квадратного уравнения в действительных числах.

a = float(input("Enter value a:"))
b = float(input("Enter value b:"))
c = float(input("Enter value c:"))

d = b**2-4*a*c
if d < 0:
    print("Equation has no real roots.")
elif d == 0:
    if a == 0:
        print("Not square equation")
    else:
        x = -b/(2*a)
        print("Equation has unique solution", x)
else:
    if a == 0:
        print("Not square equation")
    else:
        x1 = (-b+d**0.5)/(2*a)
        x2 = (-b-d**0.5)/(2*a)
        print("Equation has two roots:", x1, x2)