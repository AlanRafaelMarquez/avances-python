namespace Entrada_de_datos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Introduzca su nombre: ");
            string nombre = Console.ReadLine();
            Console.WriteLine("Introduzca su edad: ");
            int edad = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Ingrese su salario: ");
            double salario = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("El nombre es: " + nombre);
            Console.WriteLine("La edad es: "+edad);
            Console.WriteLine("El salario es: "+salario);  

           Console.ReadKey();
        }
    }
}
