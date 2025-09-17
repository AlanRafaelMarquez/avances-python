namespace Condicionales
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Condicional if

            Console.WriteLine("Nota final del alumno");
            
            int nota = 65;

            if (nota > 70)
            {
                Console.WriteLine("Felicidades pasaste el examen");
            }
            else if(nota < 70 &&  nota > 50 )
            {
                Console.WriteLine("Debes repetir el examen");
            }
            else
            {
                Console.WriteLine("Has reprobado el examen");
            }

                Console.ReadKey();
        }
    }
}
