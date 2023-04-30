# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#
# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)


list = [1, 3, 7, 10, 5, 8]
min = 4
max = 8

for key, value in enumerate(list):
    if min <= value <= max:
        print(f"{key}({value})")

