namespace Constante
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //En esta linea de codigo creamos una variable con var y lo imprimimos
            var numero = 10.20;
            Console.WriteLine(numero);
            numero = 3000;
            Console.WriteLine(numero);
            //En esta linea de codigo tenemos una cosntante que es inmutable o que no se puede modificar
            const int numero2 = 150;
            Console.WriteLine("Valor de la costante "+numero2);
            Console.ReadKey();
        }
    }
}
