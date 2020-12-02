#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

data=input("Give me a number:\n")
a=int(data)
aa=int(data+data)
aaa=int(data+data+data)
print(f"{a}+{aa}+{aaa}={a+aa+aaa}")
