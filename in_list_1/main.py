# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#    1 2 3 4 5
#    3
#    -> 1
import random
finish_number = int(input("Введите сколько элементов должно быть в списке: "))
my_list = []
i = 1
for i in range(finish_number):
    my_list.append(random.randint(0, 10))
find_number = int(input(
    "Введите число которое хотите найти сколько раз оно встречается в нашем списке: "))
count = 0
for i in range(len(my_list)):
    if (find_number == my_list[i]):
        count += 1
print(f"В списке {my_list} число {find_number} встречается {count} раз")