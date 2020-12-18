# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# import sys
# def type():
#     global line
#     line=input("Введите текст:\n")
#     if line == "":
#         print("Программа завершена")
#         sys.exit()
#     else:
#         return line
#
# with open("test.txt", "w") as file:
#     file.writelines(type())
#
with open("test.txt", "w") as file:
    while True:
        line = input("Введите текст:\n")
        if line == "":
            print("Программа завершена")
            break
        file.writelines(line)
