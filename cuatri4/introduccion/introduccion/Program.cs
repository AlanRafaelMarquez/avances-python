using System;
using System.Runtime.CompilerServices;

namespace introduccion
{
    internal class Program
    {
        static void Main(string[] args)
        {
            
                Console.WriteLine("Dime tu edad");
                int edad = 0;
        reintento:
            try
            {
                edad = int.Parse(Console.ReadLine());
            }
            catch
            {
                Console.WriteLine("No es una edad correcta, vuelve a intentar");
                goto reintento;
            }
            if (edad < 18)
                goto skip;
                Console.WriteLine("Dime que bebida quieres");
                string bebida = Console.ReadLine();
                Console.Write($"Hola tu bebida es: " + bebida + "\nLa edad es: " + edad );
                Console.ReadKey();
        skip:
            ;
        }   
    }
}
