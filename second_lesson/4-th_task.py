#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

data = input("Введи строку:\n")
list = data.split(" ")
i=1
for word in list:
    if len(word) > 10:
        word = word[0:10]
    print(f"{i}. {word}")
    i+=1