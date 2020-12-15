# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint

list=[]
i=0
while i<50:
    a= randint(0, 40)
    list.append(a)
    i+=1
print(f"Initial list:\n{list}")
new_list = [b for b in list if list.count(b) == 1]
print(f"Cleaned list:\n{new_list}")