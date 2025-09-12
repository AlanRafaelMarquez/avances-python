using System;
namespace ejercicio1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Dime la primera edad");
            int edad1 = 0;
            edad1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Dime la segunda edad");
            int edad2 = 0;
            edad2 = int.Parse(Console.ReadLine());
            Console.WriteLine("Dime la primera altura");
            double altura1 = 0;
            altura1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Dime la segunda altura");
            double altura2 = 0;
            altura2 = int.Parse(Console.ReadLine());
            Console.WriteLine("Dime el primer peso");
            double peso1 = 0;
            peso1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Dime el segudo peso");
            double peso2 = 0;
            peso2 = int.Parse(Console.ReadLine());
            if (edad1 >= edad2)
            {
                Console.WriteLine("La primera persona es mayor de edad");
            }
            else
            {
                Console.WriteLine("La segunda persona es mayor edad");
            }
            if (altura1 >= altura2)
            {
                Console.WriteLine("La primera persona es mas alto");
            }
            else
            {
                Console.WriteLine("La segunda persona es mas alto");
            }
            if (peso1 >= peso2)
            {
                Console.WriteLine("La primera persona tiene menor indice de masa corporal");
            }
            else
            {
                Console.WriteLine("La segunda persona tiene menor indice de masa corporal");
            }
        }
    }
}
