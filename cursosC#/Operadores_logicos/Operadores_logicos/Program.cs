namespace Operadores_logicos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int numero1 = 400, numero2 = 90, numero3 = 50;
            bool resultado;

            //Operaor ADN (Y)
            resultado = numero1 < numero2 && numero1 < numero3;
            Console.WriteLine(resultado);

            //Operor OR (O)
            resultado = numero1 < numero2 || numero1 < numero3;
            Console.WriteLine(resultado);

            //Operor Not (NO)
            resultado = numero1 < numero2 || numero1 < numero3;
            Console.WriteLine(!resultado);

             
            Console.ReadKey();  
        }
    }
}
