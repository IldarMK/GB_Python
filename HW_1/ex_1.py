# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

num = input('Enter day number 1-7: ')

while not (num.isdigit() and int(num) > 0 and int(num) < 8):
    print('Day number must be 1-7')
    num = input('Enter day number 1-7: ')

print(f'{num} ->', end=' ')
if num in ('6', '7'):
    print('Yes')
else:
    print('No')