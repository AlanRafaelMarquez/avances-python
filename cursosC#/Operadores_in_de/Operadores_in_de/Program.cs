namespace Operadores_in_de
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int numero = 5;
            Console.WriteLine("Valor origina: " + numero);
            //+= se usa para incrementar o decrementar valores especificos  tambien se puede usar con operador aritmetico
            numero++;
            Console.WriteLine("Valor incrimentado: " + numero);
            numero--;
            Console.WriteLine("Valor Decremento: " + numero);

            int valor = 7;
            int valor2 = ++valor;

            Console.WriteLine(valor2);


            Console.ReadKey();
        }
    }
}
