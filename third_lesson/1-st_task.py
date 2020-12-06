# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError as err:
        print("Who the F*** divides by zero?\n", err)

arg1 = float(input("Введите первое число:\n"))
arg2 = float(input("Введите второе число:\n"))

print(func(arg1, arg2))