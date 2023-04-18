# *Задача 20: * В настольной игре Скрабл (Scrabble)
# каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

one = frozenset(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"])
two = frozenset(['D', 'G', "Д", "К", "Л", "М", "П", "У"])
three = frozenset(['B', 'C', 'M', 'P', "Б", "Г", "Ё", "Ь", "Я"])
four = frozenset(['F', 'H', 'V', 'W', 'Y', "Й", "Ы"])
five = frozenset(['K', "Ж", "З", "Х", "Ц", "Ч"])
eight = frozenset(['J', 'X', "Ш", "Э", "Ю"])
ten = frozenset(['Q', 'Z', "Ф", "Щ", "Ъ"])

point = {
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    eight: 8,
    ten: 10
}
res = 0

str = input().upper()
list_str = []
for i in str:
    list_str.append(i)

for el in list_str:
    if el in one:
        res += point[one]
    elif el in two:
        res += point[two]
    elif el in three:
        res += point[three]
    elif el in four:
        res += point[four]
    elif el in five:
        res += point[five]
    elif el in eight:
        res += point[eight]
    elif el in ten:
        res += point[ten]

print(res)