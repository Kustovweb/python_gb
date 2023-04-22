# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

num = int(input("Введите число "))
deg = int(input("Введите степень числа "))


def pow_1(num, deg):
    if deg == 1:
        return num
    else:
       return pow(num, deg - 1) * num


print(pow_1(num, deg))
