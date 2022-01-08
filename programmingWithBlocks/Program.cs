void Greeting()
{
    Console.WriteLine("Здравствуйте, дорогой друг. Данная программа представляет из себя игру, в которой вам необходимо будет отгадать число");
    Console.WriteLine("Чтобы сгенерировать число, введите последовательно верхнюю и нижнюю границу диапазона возможных чисел");
}
int CreateNumber(int result = 0)
{
    Console.WriteLine("Верхняя граница:");
    int high = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Нижняя граница:");
    int low = Convert.ToInt32(Console.ReadLine());
    Random r = new Random();
    result = r.Next(low, high);
    return result;
}


Greeting();
Console.WriteLine("Для того чтобы угадать число у вас есть 10 попыток" );
int num = CreateNumber(0);
int move(int motion = 10)
{ 
    while (motion > 0)
    {
        Console.WriteLine("Введите число:");
        int isk = Convert.ToInt32(Console.ReadLine());
        if (isk == num) 
        {
            Console.WriteLine("Вы угадали! Браво!");
            motion = 0;
            return motion;
        }
        if (isk > num)
            {
                Console.WriteLine("Ваше число больше загаданного");
            }
            else
            {
                Console.WriteLine("Ваше число меньше загаданного");
            }
        
            Console.WriteLine($"Вы не угадали, осталось {motion--} попыток");
    }
        Console.WriteLine($"Ваши попытки закончились, а число так и не было угадано. Это было число {num}");
        return motion;
}
move(10);


