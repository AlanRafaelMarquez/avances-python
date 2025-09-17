namespace Operadores_comparacion
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int a = 10, b = 20;
            string resultado;
            //Operador mayor que
            resultado = (a > b) ? "Si" : "No";
            Console.WriteLine(resultado);
            //Operador menor que
            resultado = (a < b) ? "Si" : "No";
            Console.WriteLine(resultado);
            //Operador igual que
            resultado = (a == b) ? "Si" : "No";
            Console.WriteLine(resultado);
            //Operador mayor o igual que
            resultado = (a >= b) ? "Si" : "No";
            Console.WriteLine(resultado);
            //Operador menor o igual que
            resultado = (a <= b) ? "Si" : "No";
            Console.WriteLine(resultado);
            //Operador distinto que
            resultado = (a != b) ? "Si" : "No";
            Console.WriteLine(resultado);
            Console.ReadKey();  
        }
    }
}
