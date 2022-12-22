# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num = input('Enter number 1-4: ')

num = int(num)
if num == 1:
    print('Coordinates 1 quarter: X(0;∞) and Y(0;∞)')
elif num == 2:
    print('Coordinates 2 quarter: X(-∞;0) and Y(0;∞)')
elif num == 3:
    print('Coordinates 3 quarter: X(-∞;0) and Y(-∞;0)')
else:
    print('Coordinates 4 quarter: X(0;∞) and Y(-∞;0)')