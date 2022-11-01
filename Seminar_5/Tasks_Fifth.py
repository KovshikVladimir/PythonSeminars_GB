# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'Мы абв очень оченьабв абв любим Питон!'
# my_list = text.split(' ')
# final_list = []
# print(my_list)

# for i in my_list:
#     if i.find('абв') == -1:
#         final_list.append(i)
# print(final_list)

# # альтернатива
# text = 'Мы абв очень оченьабв абв любим Питон!'.split()
# smb = 'абв'

# print(text)
# print(' '.join([word for word in text if smb not in word]))
# # Filter метод
# text = 'Мы абв очень оченьабв абв любим Питон!'.split()
# smb = 'абв'

# print(text)
# # (filter(lambda word: smb not in word,text))
# print(' '.join(list(filter(lambda word: smb not in word,text))))


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

#Игрок против игрока
# sweets = 20
# while sweets > 0:
#     n = int(input('Игрок 1 введите число от 1 до 28 : '))
#     if n > 28 or n < 0:
#         print('Введите корректное число.')
#     else:
#         sweets -= n
#         if sweets <= 0:
#             print('Победил игрок 1!')
#             break
#         else: 
#             print(f'Оставшиеся конфеты: {sweets}')  
#     n = int(input('Игрок 2 введите число от 1 до 28 : '))
#     if n > 28 or n < 0:
#         print('Введите корректное число.')
#     else:
#         sweets -= n
#         if sweets <= 0:
#             print('Победил игрок 2!')
#             break
#         else: 
#             print(f'Оставшиеся конфеты: {sweets}')  

#Игрок против бота
from random import randint
from re import X

# sweets = 20
# while sweets > 0:
#     n = int(input('Игрок 1 введите число от 1 до 28 : '))
#     if n > 28 or n < 0:
#         print('Введите корректное число.')
#     else:
#         sweets -= n
#         if sweets <= 0:
#             print('Ты победил!')
#             break
#         else: 
#             print(f'Оставшиеся конфеты: {sweets}')  
#     n = randint(1,29)
#     print(f'Игрок 2 делает свой ход')
#     if n > 28 or n < 0:
#         print('Введите корректное число.')
#     else:
#         sweets -= n
#         if sweets <= 0:
#             print('Победил робот, человечество обречено')
#             break
#         else: 
#             print(f'Оставшиеся конфеты: {sweets}')  

#Игрок против умного бота
# sweets = 201
# while sweets > 0:
#     if sweets%29 == 0:
#         n = 28
#     else:
#         n = randint(1,29)
#     print(f'Игрок 2 делает свой ход')
#     if n > 28 or n < 0:
#         print('Введите корректное число.')
#     else:
#         sweets -= n
#         if sweets <= 0:
#             print('Победил робот, человечество обречено')
#             break
#         else: 
#             print(f'Оставшиеся конфеты: {sweets}') 
#     n = int(input('Игрок 1 введите число от 1 до 28 : '))
#     if n > 28 or n < 0:
#         print('Введите корректное число.')
#     else:
#         sweets -= n
#         if sweets <= 0:
#             print('Ты победил!')
#             break
#         else: 
#             print(f'Оставшиеся конфеты: {sweets}')  


# # 3. Создайте программу для игры в ""Крестики-нолики"".
# def select_position(x):
#     if x == 'a':
#         a == ' O '
#     if x == 'b':
#         b = ' O '
#     if x == 'c':
#         c = ' O '
#     if x == 'd':
#         d = ' O '
#     if x == 'e':
#         e = ' O '
#     if x == 'f':
#         f = ' O '
#     if x == 'g':
#         g = ' O '
#     if x == 'h':
#         h = ' O '
#     if x == 'i':
#         i = ' O '
#     return x


# a = ' A '
# b = ' B '
# c = ' C '
# d = '-D-'
# e = '-E-'
# f = '-F-'
# g = ' G '
# h = ' H '
# i = ' I '
# print(f'{a}|{b}|{c}')
# print(f'{d}|{e}|{f}')
# print(f'{g}|{h}|{i}')

# counter = 8
# while counter >=0:
#     n = input('Игрок 1 - Введите букву нужной клетки:')
#     if n == 'a':
#         a = ' O '
#     if n == 'b':
#         b = ' O '
#     if n == 'c':
#         c = ' O '
#     if n == 'd':
#         d = ' O '
#     if n == 'e':
#         e = ' O '
#     if n == 'f':
#         f = ' O '
#     if n == 'g':
#         g = ' O '
#     if n == 'h':
#         h = ' O '
#     if n == 'i':
#         i = ' O '
#     counter-=1
#     print(f'{a}|{b}|{c}')
#     print(f'{d}|{e}|{f}')
#     print(f'{g}|{h}|{i}')
#     if a == b == c == ' O ':
#         print('Победил первый игрок!')
#         break
#     if d == e == f == ' O ':
#         print('Победил первый игрок!')
#         break
#     if g == h == i == ' O ':
#         print('Победил первый игрок!')
#         break
#     if a == d == g == ' O ':
#         print('Победил первый игрок!')
#         break
#     if b == e == h == ' O ':
#         print('Победил первый игрок!')
#         break
#     if c == f == i == ' O ':
#         print('Победил первый игрок!')
#         break
#     if a == e == i == ' O ':
#         print('Победил первый игрок!')
#         break
#     if g == e == c == ' O ':
#         print('Победил первый игрок!')
#         break
    
#     if a == b == c == ' X ':
#         print('Победил второй игрок!')
#         break
#     if d == e == f == ' X ':
#         print('Победил второй игрок!')
#         break
#     if g == h == i == ' X ':
#         print('Победил второй игрок!')
#         break
#     if a == d == g == ' X ':
#         print('Победил второй игрок!')
#         break
#     if b == e == h == ' X ':
#         print('Победил второй игрок!')
#         break
#     if c == f == i == ' X ':
#         print('Победил второй игрок!')
#         break
#     if a == e == i == ' X ':
#         print('Победил второй игрок!')
#         break
#     if g == e == c == ' X ':
#         print('Победил второй игрок!')
#         break
#     if counter <= 0:
#         break
#     n = input('Игрок 2 - Введите букву нужной клетки:')
#     if n == 'a':
#         a = ' X '
#     if n == 'b':
#         b = ' X '
#     if n == 'c':
#         c = ' X '
#     if n == 'd':
#         d = ' X '
#     if n == 'e':
#         e = ' X '
#     if n == 'f':
#         f = ' X '
#     if n == 'g':
#         g = ' X '
#     if n == 'h':
#         h = ' X '
#     if n == 'i':
#         i = ' X '
#     print(f'{a}|{b}|{c}')
#     print(f'{d}|{e}|{f}')
#     print(f'{g}|{h}|{i}')

#     if a == b == c == ' O ':
#         print('Победил первый игрок!')
#         break
#     if d == e == f == ' O ':
#         print('Победил первый игрок!')
#         break
#     if g == h == i == ' O ':
#         print('Победил первый игрок!')
#         break
#     if a == d == g == ' O ':
#         print('Победил первый игрок!')
#         break
#     if b == e == h == ' O ':
#         print('Победил первый игрок!')
#         break
#     if c == f == i == ' O ':
#         print('Победил первый игрок!')
#         break
#     if a == e == i == ' O ':
#         print('Победил первый игрок!')
#         break
#     if g == e == c == ' O ':
#         print('Победил первый игрок!')
#         break
    
#     if a == b == c == ' X ':
#         print('Победил второй игрок!')
#         break
#     if d == e == f == ' X ':
#         print('Победил второй игрок!')
#         break
#     if g == h == i == ' X ':
#         print('Победил второй игрок!')
#         break
#     if a == d == g == ' X ':
#         print('Победил второй игрок!')
#         break
#     if b == e == h == ' X ':
#         print('Победил второй игрок!')
#         break
#     if c == f == i == ' X ':
#         print('Победил второй игрок!')
#         break
#     if a == e == i == ' X ':
#         print('Победил второй игрок!')
#         break
#     if g == e == c == ' X ':
#         print('Победил второй игрок!')
#         break

#     if counter <= 0:
#         break
#     else:
#         counter-=1
    

# # 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# data = 'aaabbbwww'

# a_count = data.count('a')
# b_count = data.count('b')``
# w_count = data.count('w')

# print(f'{a_count}a{b_count}b{w_count}w')

