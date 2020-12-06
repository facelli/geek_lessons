# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    elif c < a and c < b:
        return a + b


data = (input("Введите через пробел три числа:\n")).split(" ")
a = int(data[0])
b = int(data[1])
c = int(data[2])
print(f"сумма наибольших двух:\n {my_func(a, b, c)}")