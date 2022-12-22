# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = input('Enter coord X: ')
y = input('Enter coord Y: ')

if x == '0' and y == '0':
    print('Error. Point in the center ')
elif x == '0':
    print (f'Point on the X')
elif y == '0':
    print (f'Point on the Y')
else:
    x = float(x)
    y = float(y)
    print (f'({x}; {y})', end=' -> ')
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)