print("Введите первую точку")

x1 = float(input('X: '))

y1 = float(input('Y: '))

print("Введите вторую точку")

x2 = float(input('X: '))

y2 = float(input('Y: '))



x_diff = x2 - x1

y_diff = y2 - y1

if x_diff == 0:
    b = x1

    print("Уравнение прямой проходящей через эти точки выходит: ")

    print("y = ", b)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Уравнение прямой проходящей через эти точки получается:")
    print("y = ", k, " * x + ", b)
