
action = input("Введите операцию: ")
amount = int(input("Сколько операндов?"))
for order in range(1, amount + 1):
    number = int(input("Введите операнд", str(order) + ":"))










if action == "X" or action == "*":
    print(A, action, B, "=", A * B)
elif action == "/":
    print(A, action, B, "=", A / B)
elif action == "+":
    print(A, action, B, "=", A + B)
elif action == "-":
    print(A, action, B, "=", A - B)

while action != "X" and action != "*" and action != "/" and action != "+" and action != "-":
    print("Ошибка! Повторите ввод!")
    action = input("Введите операцию: ")
    A = int(input("Введите первое число: "))
    B = int(input("Введите второе число: "))


