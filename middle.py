import random
print(' Введите число от 23 до 40 включительно')

task = int(input())
if task == 23:
    print('Введите N, чтобы увидеть табоицу квадратов от 1 до N')
    n = int(input())
    while n>0:
        print(n**2)
        n = n-1
elif task == 24:
    print('Введите N, чтобы увидеть кубы чисел от 1 до N')
    n = int(input())
    while n>0:
        print(n**3)
        n = n-1
elif task == 25:
    print('Введите N, чтобы узнать сумму чисел от 1 до N')
    n = int(input())
    sum = 0
    while n>0:
        sum = n + sum
        n = n-1
    print(f'Сумма чисел от 1 до N равна{sum}')
elif task == 26:
    print('Введите числа А и В, чтобы возвести А в натуральную степень В')
    a = int(input())
    b = int(input())
    mult = 1
    while b>0:
        mult = mult * a
        b = b - 1
    print(f'А в степени В равняется {mult}')
elif task == 27:
    print('Введите число, чтобы узнать количество цифр в нём')
    n = int(input())
    if n>0:
        length = len(str(n))
        print(length)
    elif n<0:
        length = len(str(n))-1
        print(length)
    else:
        print(1)
elif task == 28:
    print('Введите число, чтобы узнать сумму его цифр')
    n = int(input())
    sum = 0
    if n>0:
        length = len(str(n))
        while length>0:
            sum = sum + n%10
            n = n//10
            length = length - 1
    elif n<0:
        length = len(str(n))-1
        while length>0:
            n = -n
            sum = sum + n%10
            n = n//10
            length = length - 1
    print(f'Сумма цифр данного числа равна {sum}')
elif task == 29:
    print('Введите N, чтобы узнать произведение всех чисел от 1 до N')
    n = int(input())
    mult = 1
    while n>0:
        mult = mult*n
        n = n - 1
    print(f'Произведение всех чисел равно {mult}')
elif task == 30:
    print('Введите N, чтобы увидеть все кубы чисел от 1 до N, заканчивающиеся на чётную цифру')
    n = int(input())
    while n>0:
        if (n**3)%2==0:
            print(n**3)
        n = n - 1
elif task == 31:
    print('Сейчас на экран будет выведен массив из 8 случайно сгенерированных элементов')
    list = []
    n = 0
    while n<9:
        list[n] = random.randint(1,100)
        n = n + 1
    print(list)
elif task == 32:
    print('Сейчас на экран будет выведен массив из 8 случайно сгенерированных элементов от 0 до 1')
    list = []
    n = 0
    while n<9:
        list[n] = random.randint(0,2)
        n = n + 1
    print(list)
elif task == 33:
    print('Сейчас на экран будет выведен массив из 12 случайно сгенерированных элементов от 0 до 9')
    list = []
    n = 0
    for i in range(12):
        list.append(random.randint(-10,10))
    print(list)
    print('Нажмите 1, чтобы найти сумму положительных элементов массива, или 2 - для отрицательных')
    n = int(input())
    sum = 0
    if n == 1:
        for i in list:
            if i>0:
                sum = sum + i
            else:
                print(i)
    if n == 2:
        for i in list:
            if i<0:
                sum = sum + i
    print(sum)
elif task == 34:
    print('Сейчас будет создан массив. Введите N, чтобы указать количество элементов в нём')
    n = int(input())
    list = []
    for i in range(n):
        list.append(random.randint(-100,100))
    print(list)
    print('Теперь каждый элемент массива будет заменяться на противоположный')
    
    for index, item in enumerate(list):
        list[index] = -item
    print(list)
elif task == 35:
    print('Введите N, чтобы указать количество элементов в массиве')
    n = int(input())
    list = []
    for i in range(n):
        list.append(random.randint(-99,99))
    print(list)
    print('Теперь введите число, которое нужно найти')
    a = int(input())
    print(f' Данное число встречается в массиве {list.count(a)} раз')
elif task == 36:
    print('Введите N, чтобы заполнить массив случайными трехзначными числами')
    n = int(input())
    list = []
    for i in range(n):
        list.append(random.randint(100,999))
    print(list)
    print('Нажмите 1, чтобы узнать количество чётных элементов в массиве и 2, чтоб узнать количество нечётных')
    ch = int(input())
    count = 0
    if ch == 1:
        for i in list:
            if i%2 == 0:
                count = count + 1
    elif ch == 2:
        for i in list:
            if i%2 != 0:
                count = count + 1
    print(f'В вашем списке {count} проверенных элементов')
elif task == 37:
    print('Сейчас будет задан массив из 123-х элементов. Программа находит количество элементов из отрезка [10,99]')
    list = []
    for i in range(123):
        list.append(random.randint(-1000,1000))
    print(list)
    count = 0
    list2 = []
    for i in list:
        if i>=10 and i<=99:
            count = count + 1
            list2.append(i)
    print(f'Данных элементов в массиве {count}')
    print(list2)
elif task == 38:
    print('Введите N, чтобы заполнить массив случайными числами')
    n = int(input())
    list = []
    for i in range(n):
        list.append(random.randint(-100,100))
    print(list)
    print('Программа находит сумму чисел, стоящих на нечётной позиции')
    sum = 0
    for index, item in enumerate(list):
        if index%2==0:
            sum = sum + item
            print(sum)
    print(f'Сумма равна {sum}')
elif task == 39:
    print('Введите N, чтобы задать количество элементов в массиве')
    n = int(input())
    list = []
    for i in range(n):
        list.append(random.randint(-1000,1000))
    print(list)
    print('А сейчас программа посчитает произведение пар чисел этого массива и выведет на экран')
    count1 = 0
    count2 = -1
    mult = 1
    for i in range(n//2):
        mult = list[count1] * list[count2]
        count1 = count1 + 1
        count2 = count2 - 1
        print(mult)
elif task == 40:
    print('Введите N, чтобы задать количество элементов в массиве')
    n = int(input())
    list = []
    for i in range(n):
        list.append(random.randint(-1000,1000))
    print(list)
    print('Данная программа находит разницу между максимальным и минимальным элементом в массиве')
    print(f'Разница равна {max(list) - abs(min(list))}')