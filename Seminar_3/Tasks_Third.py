# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# use_list = [2, 5, 5, 1000, 3]
# counter = 0
# summa = 0
# for i in range(len(use_list)):
#     if i % 2 != 0:
#         summa += use_list[i]
# print(summa)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# base_list = [2, 3, 5, 6, 5, 6, 2, 3]
# final_list = []

# if len(base_list) % 2 != 0:
#     counter = len(base_list)-1
#     index = 0
#     while index != counter:
#         resulting = base_list[index] * base_list[counter]
#         counter = counter - 1
#         index += 1
#         final_list.append(resulting)
#     resulting = base_list[index] * base_list[index]
#     final_list.append(resulting)
# else:
#     counter = len(base_list)-1
#     index = 0
#     while index < counter:
#         resulting = base_list[index] * base_list[counter]
#         counter = counter - 1
#         index += 1
#         final_list.append(resulting)
# print(final_list)

# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# list_final = [1.1, 1.2, 3.1, 10.01]
# min_part = list_final[0]
# max_part = 0

# for i in list_final:
#     if i * 10 % 10 > max_part:
#         max_part = i
#     elif i * 10 % 10 < min_part:
#         min_part = i
# result = (((max_part * 10 - min_part * 10) % 10) * 10) / 100
# print(max_part)
# print(min_part)
# print(round(result, 3))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# number = int(input('Введите число: '))
# resulting_list = []
# while number > 0:
#     res = number % 2
#     number //= 2
#     resulting_list.append(res)
# final_resulting = []
# temp_len = len(resulting_list) - 1
# while temp_len >= 0:
#     final_resulting.append(resulting_list[temp_len])
#     temp_len -= 1
# print(final_resulting)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# number = int(input('Введите число: '))
# resulting_list = []
# f1 = 0
# f2 = 1
# for i in range(number):
#     f1, f2 = f2, f1+f2
#     resulting_list.append(f1)
# final_list = resulting_list[:]
# for i in range(1,len(resulting_list),2):
#     final_list[i] = -final_list[i]
# final_list = final_list[::-1]
# print(final_list + [0] + resulting_list)
