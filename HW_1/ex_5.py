# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09


def GetFloatValue(message):
    value = input(message)

    while not value.replace('-', '').replace('.','').isdigit():
        print('Value must be a number. Try again')
        value = input(message)
    return float(value)

def GetDistance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


x1 = GetFloatValue('Enter X coordinate for A: ')
y1 = GetFloatValue('Enter Y coordinate for A: ')
x2 = GetFloatValue('Enter X coordinate for B: ')
y2 = GetFloatValue('Enter Y coordinate for B: ')

print(f'A({x1},{y1}); B({x2},{y2}) -> {GetDistance(x1, y1, x2, y2)}')