from types import NoneType


print('Привет, это моя первая программа на питоне. Она определяет, каким преимущественно является список - положительным или отрицательным')
# Напишите функцию, которая будет принимать список чисел и проверять, 
# является ли он преимущественно положительным (вывод — True или False).


list = [] 
N = int(input('Введите размер первого списка с клавиатуры:')) 
for x in range(N): 
    x = input('Вводите данные:') 
    try: list.append(int(x))
    except ValueError: list.append(x)
def func(list):
    i = 0
    count1 = 0
    count2 = 0
    for i in list:
        if i>=0:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    if count1>count2:
        return 'Положительных чисел в списке больше'
    if count2>count1:
        return 'Отрицательных чисел в списке больше'
    if count2==count1:
        return 'Положительных и отрицательных чисел в списке поровну'
print(func(list))

