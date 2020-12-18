# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.

dict = {"One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре"
        }
with open("4-th_task.txt", "r") as file:
    with open("4-th_task2.txt", "w") as file2:
        lines = file.readlines()
# print((lines[0]).split(" — "))
        for line in lines:
            line = line.split(" — ")
            file2.write(f"{dict[line[0]]} - {line[1]}")
