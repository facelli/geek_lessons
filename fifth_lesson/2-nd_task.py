# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

with open("2-nd_task.txt", "r") as file:
    lines=file.readlines()
print(f"В файле {len(lines)} строк.")
i=1
for line in lines:
     line = line.split()
     print(f"В {i} строке {len(line)} слов.")
     i+=1