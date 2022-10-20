# 1. Вычислить число c заданной точностью d
# import math

# a = input('Введите кол-во знаков после запятой: ')
# counter = 0
# for i in a:
#     if i != ',':
#         counter +=1
# print(round(math.pi,counter-1))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число N: '))
# resulting_list = []
# counter = 2
# while (counter <= n):
#     if (n % counter) == 0:
#         resulting_list.append(counter)
#         n = n/counter
#     else:
#         counter += 1
# print(resulting_list)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# given_list = [1, 2, 3, 4, 4, 12, 4, 1, 6, 1, 3, 5, 1, 2, 7, 1, 3, 5, 7, 9]
# result_list = []

# counting = 0
# while counting < len(given_list):
#     using_counter = 0
#     for i in given_list:
#         if i == given_list[counting]:
#             using_counter += 1
#     if using_counter == 1:
#         result_list.append(given_list[counting])
#         counting += 1
#     else:
#         counting += 1
# print(result_list)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффицентов многочлена и записать в файл многочлен степени k.

# from random import randint, random

# from macpath import split

# k = 2
# resulting_file = f'Result.txt'

# with open(resulting_file,'w') as f:
#     if k == 2:
#         f.write(f'{randint(0,100)} * x^{k} + {randint(0,100)} * x^{k-1} + {randint(0,100)} = 0')
#     else:
#         f.write(f'{randint(0,100)} * x^{k} + {randint(0,100)} * x^{k-1} + {randint(0,100)} * x^{k-2} = 0')

# 5. Даны два файла, в каждом из которых находится запись многочена. Задача - сформировать файл, содержащий сумму многочленов.

second_list = []
first_list = []
with open('First.txt','r') as f:
    first_list = f.read()
with open('Second.txt','r') as f:
    second_list = f.read()

first_list = first_list.split()
second_list = second_list.split()

sum_1 = int(first_list[0]) + int(second_list[0]) 
sum_2 = int(first_list[4]) + int(second_list[4])
sum_3 = int(first_list[8]) + int(second_list[8])

with open('Resulting.txt','w') as d:
    d.write((f'{sum_1} * x^{2} + {sum_2} * x + {sum_3} = 0'))

