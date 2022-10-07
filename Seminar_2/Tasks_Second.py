# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# number = input('Введите вещественное число: ')
# total = 0
# for i in number:
#     if i.isdigit():
#         total += int(i)
# print(total)


# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.

# n = int(input('Введите число N: '))
# count = 1
# final = 1
# list1 = []
# list1.append(final)
# while count < n:
#     final *= count+1
#     count += 1
#     list1.append(final)
# print(list1)


# Задайте список из n чисел последовательности
# (1 + 1 \ n)^n и выведите на экран их сумму.

# n = int(input('Введите число N: '))
# count = 1
# final = 0
# list2 = []
# while count <= n:
#     result = pow((1+1/count), count)
#     list2.append(round(result,3))
#     final += result
#     count += 1
# print(list2)
# print(round(final,3))


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся через пробел в одной строкой.
# n = 3



# n = int(input('Введите число N: '))
# list3 = []
# finals = 1
# for i in range(-n,n):
#     list3.append(i)
# print(list3)

# row = input('Введите номера позиций элементов через пробел: ')
# resulting_list = row.split(' ')
# print(resulting_list)
# for e in resulting_list:
#     finals *= list3[int(e)]
# print(f'Произведение элементов на указанных позициях = {finals}')

# Реализуйте алгоритм перемешивания списка.
# import random

# final_list = [1,2,3,4,5,6,7,8]
# random.shuffle(final_list)
# print(final_list)
