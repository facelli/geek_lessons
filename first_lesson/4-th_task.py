# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

data=input("Give me a number:\n")
try:
    a = int(data)
    b=a%10
    a=a//10
    while a>0:
        if a%10>b:
            b=a%10
        a=a//10
    print(f"Biggest charachter is {b}")
except Exception as err:
    print(f"I said, give me a number! Digits, you know?\nError: {err}")