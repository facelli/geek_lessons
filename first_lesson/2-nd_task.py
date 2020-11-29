#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

data=input("Give me seconds!\n")
seconds=int(data)
h=seconds//3600
m=(seconds%3600)//60
s=seconds%60
print(f"Who counts seconds? Here, be a normal person!\n{h:02}:{m:02}:{s:02}")