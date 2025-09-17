namespace Operadores_aritmeticos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int valor1 = 90, valor2 = 70, valor3 = 10;
            //operador de suma
            int total = valor1 + valor2;
            Console.WriteLine("Total de la suma: " + total);

            //Resta
            int diferencia = valor1 - valor2;
            Console.WriteLine("Total de la resta : " + diferencia);

            //Multiplicacion
            int producto = valor3 + valor2;
            Console.WriteLine("Producto: " + producto);

            //Division
            int resultado = valor1 / valor3;
            Console.WriteLine("Resultado: " + resultado);

            //residuo
            var modulo = valor2 % valor3;
            Console.WriteLine("Residuo: "+modulo);
            Console.ReadKey();
            
        }
    }
}
