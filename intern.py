from operator import truediv
import math

print('Введите номер задачи от 0 до 22 включительно')

task = int(input())
if task == 0:
    print('Введите число, чтобы узнать его квадрат')
    kv = int(input())
    kv = kv ** 2
    print('Квадрат числа равен', kv)
elif task == 1:
    print('Введите два числа, чтобы узнать, является ли первое квадратом второго')
    a = int(input())
    b = int(input())
    if a == b**2:
        print('Число', a, 'является квадратом числа', b)
    else:
        print('Число', a, 'не является квадратом числа', b)
elif task == 2:
    print('Введите два числа, чтобы узнать наибольшее и наименьшее из них')
    a = int(input())
    b = int(input())
    if a>b:
        print('Наибольшее число', a, ', а наименьшее -', b)
    elif a<b:
        print('Наибольшее число', b, ', а наименьшее -', a)
    else:
        print('Числа равны друг другу')
elif task == 3:
    print('Выберите номер дня недели от 1 до 7, чтобы вывести его название на экран')
    numweek = int(input())
    if numweek == 1:
        print('Понедельник')
    elif numweek == 2:
        print('Вторник')
    elif numweek == 3:
        print('Среда')
    elif numweek == 4:
        print('Четверг')
    elif numweek == 5:
        print('Пятница')
    elif numweek == 6:
        print('Суббота')
    elif numweek == 7:
        print('Воскресенье')
    else:
        print('Задание было - ввести число от 1 до 7. Вы кажись не справились.')
elif task == 4:
    print('Найти максимальное из 3-х чисел')

    a = int(input())
    b = int(input())
    c = int(input())

    print('Максимальное из 3х чисел:',max(a,b,c))
elif task == 6:
    print('Введите число, чтобы узнать, является ли оно чётным')
    n = int(input())
    def ParityCheck(n):
        if n % 2 == 0:
            print(f'Число {n} - чётное')
        else:
            print(f'Число {n} - нечётное')
        return None
    ParityCheck(n)
elif task == 7:
    print('Введите N, чтобы на экран была выведена целочисленная последовательность от -N до N')
    n = -int(input())
    count = 0
    list=[]
    lim = -n*2+1
    while count<lim:
        list.append(f'{n}')
        n += 1
        count +=1
    print(list)
elif task == 8:
    print('Введите N, чтобы увидеть последовательность всех чётных чисел от 1 до N')
    n = int(input())
    def func(n):
        for i in range(2,n+1,2):
            print(i)
        return None
    func(n)
elif task == 9:
    print('Введите трёхзначное число, чтобы узнать его последнюю цифру')
    num = int(input())
    num = num % 10 
    print (num)
elif task == 10:
    print('Введите трёхзначное число, чтобы узнать его вторую цифру')
    num = int(input())
    num = num // 10
    num = num % 10
    print (num)
elif task == 11:
    print('Введите число из отрезка [10, 99], чтобы узнать наибольшую цифру числа')
    num = int(input())
    n2 = num % 10
    n1 = num // 10
    if n1>n2:
        print(f'Первая цифра числа {num} больше второй')
    elif n2<n1:
        print(f'Вторая цифра числа {num} больше первой')
    else:
        print('Обе цифры в числе равны')
elif task == 12:
    print('Введите трёхзначное число, чтобы удалить его вторую цифру')
    num = int(input())
    ost = num//10
    ost2 = num%10
    ost = ost//10
    num = int(str(ost)+str(ost2))
    print(num)
elif task == 13:
    print('Введите два числа, чтобы узнать кратно ли первое второму. Если нет - будет выведен остаток от деления')
    a = int(input())
    b = int(input())
    if a % b == 0:
        print('Первое число кратно второму!')
    elif a % b != 0:
        print(f'Первое число не кратно второму. Остаток от деления равен {a%b}')
elif task == 14:
    print('Введите число, чтобы найти его третью цифру')
    num = input()
    if int(num)>99:
        num = num[2]
        print(f'Третья цифра числа: {num}')
    elif int(num)<-99:
        num = num[3]
        print(f'Третья цифра числа: {num}')
    else:
        print('У данного числа нет третьей цифры, так как оно меньше')
elif task == 15:
    print('Введите число, чтобы узнать, кратно ли оно 7-ми и 23-м')
    num = int(input())
    if num%7==0 and num%23==0:
        print('Данное число кратно 7 и 23')
    else:
        print('Данное число не кратно 7 и 23')
elif task == 16:
    print('Введите число, обозначающее день недели (от 1 до 7-ми), чтобы узнать, является ли этот день выходным')
    numweek = int(input())
    if 0<numweek<=5:
        print('Вы выбрали рабочий день')
    if 5<numweek<=7:
        print('Вы выбрали выходной день!')
elif task == 17:
    print('Введите два числа, чтобы узнать является ли первое квадратом второго')
    a = int(input())
    b = int(input())
    if a == b**2:
        print('Число', a, 'является квадратом числа', b)
    else:
        print('Число', a, 'не является квадратом числа', b)
elif task == 18:
    print('Данная программа проверяет истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y')
    print('Введите x и y')
    x = int(input())
    y = int(input())
    booll = not(x or y) == (not(x) and not(y))
    print(booll)
elif task == 19:
    print('Введите координаты точки (x и y), чтобы узнать, в какой четверти находится эта точка')
    x = int(input())
    y = int(input())

    if x>0 and y>0:
        print('Ваша точка находится в первой четверти')
    elif x<0 and y>0:
        print('Ваша точка находится во второй четверти')
    elif x<0 and y<0:
        print('Ваша точка находится в третьей четверти')
    elif x>0 and y<0:
        print('Ваша точка находится в четвёртой четверти')
elif task == 20:
    print('Задайте номер четверти (от 1-го до 4-х), чтобы узнать диапазон возможных координат')
    num = int(input())
    if num == 1:
        print('Первой четверти принадлежат числа от 0 до +бесконечности по x и y')
    if num == 2:
        print('Второй четверти принадлежат числа в диапазоне от 0 до -бесконечности по x, и от 0 до +бесконечности по y')
    if num == 3:
        print('Третьей четверти принадлежат числа в диапазоне от 0 до -бесконечности по x и y')
    if num == 4:
        print('Четвертой четверти принадлежат числа в диапазоне от 0 до +бесконечности по x, и от 0 до -бесконечности по y')
elif task == 21:
    print('Введите пятизначное число, чтобы узнать, является ли оно палиндромом')
    n1 = input("Введите целое число: ")
    n_list = list(n1)
    n_list.reverse()
    n2 = "".join(n_list)
    if n1 == n2:
        print('Данное число - палиндром')
    else:
        print('Данное число не является палиндромом')
elif task == 22:
    print('Введите координаты 2х точек, чтобы узнать их расстояние в 3d пространстве')
    print('Сначала введите координаты первой точки: x, y, z')
    x1 = int(input())
    y1 = int(input())
    z1 = int(input())
    print('Теперь введите координаты второй точки в такой же последовательности')
    x2 = int(input())
    y2 = int(input())
    z2 = int(input())
    dist = math.sqrt((max(x1,x2)-min(x1,x2))**2 + (max(y1,y2)-min(y1,y2))**2 + (max(z1,z2)-min(z1,z2))**2)
    print(f'Расстояние между этими точками равно {dist}')
