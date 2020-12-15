# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123]

from random import randint

list=[]
i=0
while i<20:
    a= randint(0, 101)
    list.append(a)
    i+=1
print(f"Generated list:\n{list}")
mod_list = [list[item] for item in range(1, len(list)) if list[item] > list[item - 1]]
print(f"Modified list:\n{mod_list}")