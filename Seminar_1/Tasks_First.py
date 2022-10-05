# Task 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# number = int(input('Введите число: '))
# if number == 6 or number == 7:
#     print('Бомба, выходной')
# elif number < 1 or number > 7:
#     print ('Ошибка, число не является днем недели')
# else:
#     print('Будние, пора на работу')

# Task 2: Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('Введите X от 0 до 1: '))
# y = int(input('Введите Y от 0 до 1: '))
# z = int(input('Введите Z от 0 до 1: '))
# if not(x or y or z) == (not(x) and not(y) and not(z)):
#     print('Утверждение истинно') 
# else:
#     print('Утверждение ложно')

# Task 3: Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x_coordinate = int(input('Введите координату X: '))
# y_coordinate = int(input('Введите координату Y: '))

# if x_coordinate == 0 or y_coordinate == 0:
#     print('X,Y не должны быть равны 0')
# elif x_coordinate > 0 and y_coordinate > 0:
#     print('Первая четверть')
# elif x_coordinate < 0 and y_coordinate > 0:
#     print('Вторая четверть')
# elif x_coordinate < 0 and y_coordinate < 0:
#     print('Третья четверть')
# elif x_coordinate > 0 and y_coordinate < 0:
#     print('Четвертая четверть')

# Task 4: Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# part_2D = int(input('Введите номер четверти:'))

# if part_2D == 1:
#     print('x [1;+∞] / y[1;+∞]')
# elif part_2D == 2:
#     print('x [-1;-∞] / y[1;+∞]')
# elif part_2D == 3:
#     print('x [-1;-∞] / y[-1;-∞]')
# elif part_2D == 4:
#     print('x [1;+∞] / y[-1;-∞]')

# Task 5: Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# from cmath import sqrt - как вариант, но мы еще это не проходили

# x1 = int(input('Введите x1: '))
# y1 = int(input('Введите y1: '))
# x2 = int(input('Введите x1: '))
# y2 = int(input('Введите y2: '))

# print(f'A [{x1},{y1}]')
# print(f'B [{x2},{y2}]')

# if x1 > x2:
#     first_line = x1 - x2
# elif x2 > x1:
#     first_line = x2 - x1
# if y1 > y2:
#     second_line = y1 - y2
# elif y2 > y1:
#     second_line = y2 - y1

# result_line = pow(first_line, 2) + pow(second_line, 2)
# final_result_line = result_line ** 0.5
# print(f'Длина отрезка = {round(final_result_line, 3)}')
