// See https://aka.ms/new-console-template for more information
void Greeting()
{
    Console.WriteLine("Здравствуйте, дорогой друг. Данная программа представляет из себя игру, в которой вам необходимо будет отгадать число");
    Console.WriteLine("Чтобы сгенерировать число, введите последовательно верхнюю и нижнюю границу диапазона возможных чисел");
}
/*int EnterHigh(int high = 100)
{
    Console.WriteLine("Верхняя граница:");
    high = Convert.ToInt32(Console.ReadLine());
    return high;
}
int EnterLow(int low = 0)
{
    Console.WriteLine("Нижняя граница:");
    low = Convert.ToInt32(Console.ReadLine());
    return low;
}*/
Greeting();
/*int high = EnterHigh();
int low = EnterLow();
Console.WriteLine(high, low);*/
int CreateNumber(int result)
{
    Console.WriteLine("Верхняя граница:");
    int high = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Нижняя граница:");
    int low = Convert.ToInt32(Console.ReadLine());
    Random r = new Random();
    result = r.Next(low, high);
    return result;
}
int num = CreateNumber(0);
Console.WriteLine(num);