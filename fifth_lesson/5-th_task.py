# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("5-th_task.txt", "w") as file:
    i = 0
    while i < 50:
        a = randint(0, 40)
        file.write(f"{str(a)} ")
        i += 1
with open("5-th_task.txt", "r") as file:
    nums = file.readlines()
    sum=0
    for num in nums:
        num=num.split()
        for item in num:
            sum+=int(item)
            # sum+=int(nums)
print(sum)