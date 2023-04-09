# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number_user = input()

index = 0
summ = 0
num_length = len(number_user)
while index < num_length:
    summ += int(number_user[index])
    index += 1

print(summ)