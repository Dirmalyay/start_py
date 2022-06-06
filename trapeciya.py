# Площадь трапеции


def trapezoid_sq(hi, b, t):
    return (t + b) / 2 * hi


def trapezoid_p(l, righ, top1, base1):
    return l + righ + top1 + base1


print("Enter parameters of trapezoid:")
lef = float(input("left side - "))
righ = float(input("right side - "))
to = float(input("top side - "))
bas = float(input("base side - "))
h = float(input("height side - "))

print("площадь равна:", trapezoid_sq(h, bas, to))
print("периметр равна:", trapezoid_p(lef, righ, to, bas))
