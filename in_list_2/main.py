# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#   1 2 3 4 5
#    6
#   -> 5

import random
import math
finish_number = int(input("Введите сколько элементов должно быть в списке: "))
my_list = []
i = 1
for i in range(finish_number):
    my_list.append(random.randint(1, 21))
find_number = int(input("Введите находимое число: "))
maxim = my_list[0]
for i in range(len(my_list)):
    if (abs(find_number-my_list[i]) < abs(find_number-maxim)):
        maxim = my_list[i]
print(
    f"Самое близкое число к числу {find_number}  из списка {my_list},  это {maxim}")
