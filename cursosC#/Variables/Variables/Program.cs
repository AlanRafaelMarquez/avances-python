namespace Variables
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Creamos una variable tipo string en la cual la llamamos Mi_nombre y almacenamos la cadena de texto "Alan"
            string Mi_nombre = "Alan";
            //Creamos una variable tipo entero la cual llamamos edad y almacenamos 18
            int edad = 18;
            //Creamos una variable tipo bool la cual la llamamos activo y almacenamos un dato flaso
            bool activo = false;
            //Cremos una variable tipo DataTime la cual la llamamos fecha y almacenamos la fecha y el tiempo actual
            DateTime fecha = DateTime.Now;
            //Creamos una variable tipo float la cual llamamos precio y almacenamos 1960.99f
            float precio = 1960.99f;
            //Creamos una variable tipo decimal la cual llamamos descuento y almacenamos 10.50m
            decimal descuento = 10.50m;

            //En esta parte del codigo imprimimos todo lo que tengo almacenado en las variables con el Console.WriteLine();
            Console.WriteLine(Mi_nombre + "\n" + edad);
            Console.WriteLine(edad);
            //Aqui cambiamos el valor de la variable para de nueva imprimirla
            edad = 19;
            Console.WriteLine(edad);
            Console.WriteLine(fecha);
            Console.WriteLine(precio);
            Console.WriteLine(descuento); 
            Console.WriteLine(activo);

            //Escribimos el Console.ReadKey(); para al momento de depurar la consola se no muestre solo que queremos imprimos
            Console.ReadKey();

        }
    }
}
