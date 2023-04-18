# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5


length = int(input("Размер массива: "))
list_1 = [int(input()) for i in range(length)]
num = int(input())
index_min_el = 0
min_diff = abs(list_1[0] - num)

for i in range(1, length):
    diff = abs(list_1[i] - num)
    if diff < min_diff:
        index_min_el = i
        min_diff = diff
print(list_1[index_min_el])
