namespace Casting
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Casting implicito
            int valor = 200;
            double total = valor;
            Console.WriteLine("Implicito: "+total);

            //Casting explicito
            double precio = 500.23;
            int descuento = (int)precio;
            Console.WriteLine("Explicito: "+descuento);

            char letra = 'A';
            int cdigoAsci = letra;
            Console.WriteLine(cdigoAsci);

            string palabra = "12345";
            int numero = Convert.ToInt32(palabra);
            Console.WriteLine(numero);

            string textoDecimal = "150.60";
            double valor3 = double.Parse(textoDecimal);
            Console.WriteLine(valor3);
            Console.ReadKey();
        } 
    }
}
