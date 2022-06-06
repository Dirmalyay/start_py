# Найти корни квадратного уравнения

a = float(input("Enter value a:"))
b = float(input("Enter value b:"))
c = float(input("Enter value c:"))
x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
print("Equation roots:", x1, x2)
