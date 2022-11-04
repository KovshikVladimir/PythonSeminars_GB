# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Seminar_2
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# ---------------------------------------------------------------------------
# number = input('Введите вещественное число: ')
# total = 0
# for i in number:
#     if i.isdigit():
#         total += int(i)
# print(total)
# ---------------------------------------------------------------------------
# def counter(f):
#     counting = 0
#     for x in range(0,len(f)):
#         counting += f[x]
#     return counting
        
# number = [x for x in range(1,int(input('Введите вещественное число: '))+1)]
# print(number)
# print(counter(number))

# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.
# ---------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------
# n = [x for x in range(1,int(input('Введите число N: '))+1)]
# list(map(int,n))
# res = 1
# for i in range(0,len(n)):
#     res *= n[i]
#     n[i] = res
# print(n)

#Semina_3
# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# ---------------------------------------------------------------------------
# use_list = [2, 5, 5, 1000, 3]
# counter = 0
# summa = 0
# for i in range(len(use_list)):
#     if i % 2 != 0:
#         summa += use_list[i]
# print(summa)
# ---------------------------------------------------------------------------
# use_list = [x for x in range(1,6)]
# working_list = list(filter(lambda x: not x%2 ==0,use_list))
# summa = 0
# for i in working_list:
#     summa += i
# print(use_list)
# print(working_list)
# print(summa)