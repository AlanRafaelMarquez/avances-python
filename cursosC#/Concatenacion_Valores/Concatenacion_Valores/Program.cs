namespace Concatenacion_Valores
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Creamos dos variables donde almacenamos un nombre y un edad en las dos variables
            string nombre = "Alan Rafael";
            int edad = 18;

            //En este linea de codigo es concatenar una cadena de carcteres con un variable con el signo de + y hacemos un salto de linea con \n
            Console.WriteLine("El nombre del usuario es: "+nombre+"\nEdad: "+edad);
            /*En esta otra linea concatenamos de otra manera al momento de imprimir con el signo de $ al princio de la cadena de caracteres
            y los imprimimos con {} una forma mejor de concatenar*/
            Console.WriteLine($"Nombre de usuario {nombre} y la edad es {edad}");
            //En esta linea imprimimos con el Console.Write la cual a diferencia del WriteLine no nos hace un salton de linea 
            Console.Write("La edad es: " + edad);

            Console.ReadKey();
        }
    }
}
