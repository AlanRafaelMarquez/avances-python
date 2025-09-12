namespace Cailificaciones
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             1)Validar sea nombre con apellido, usar funcion Contains
             2)Validar sea una calificacion validar mayor a 0, menor a 10
             3)Hacer un maximo de 3 intentos de captura
            -Los intentos se resetean a 0 como una captura exitosa
            -De fallar, la captura dice "No capturarlo" y poner 0
            Bonus
            -Omitir las sumas no capturadas y resetear el conteo de los estudiantes
             */

            //Definimos la variable que maxima para reprobar 
            double fail = 7;
            //Capturamos que cantidad de alumnos queresmos registrar y preguntar
            Console.WriteLine("Cuantos alumnos son: ");
            int alumnCount = int.Parse(Console.ReadLine());
            //El nombre del alumno lo capturamos en un arreglo
            string[] names = new string[alumnCount];
            //La calificacion del alumno lo capturamos en un arreglo
            double[] grades = new double[alumnCount];

          

            //Iniciamos un contador
            int counter = 0;
            //Iniciamos un while que el contador a imprimir hasta el numero de alumnos que pedimos
            while (counter < alumnCount)
            {
                int error = 3;
                while (error > 0) {

                    //Pedimos el nombre del alumno y los vamos haciedo que se sume al momento de imprimir y tambien pedimos la calificacion
                    Console.WriteLine($"Proporcina el nombre del alumno N° {counter + 1}");
                    names[counter] = Console.ReadLine();
                    if (!names[counter].Contains(" ")) {
                        Console.WriteLine("El nombre no tiene apellido");
                        error--;
                        continue;
                    }
                    Console.WriteLine($"Proporcina la calificacion del alumno N° {counter + 1}");
                    grades[counter] = double.Parse(Console.ReadLine());
                    if (!(grades[counter] > 0 && grades[counter] < 11)) {
                        Console.WriteLine("La calificacion esta fuera de rango");
                        error--;
                        continue;
                    }
                    break;
                }
                if (error == 0)
                {
                    Console.WriteLine("Exedio el limite de errores");
                    names[counter] = "No capturado";
                    grades[counter] = 0;
                }
                //Cual quier de estas forma es correcta para incrementar la variable
                counter++;
                //counter = counter + 1;
                //counter += 1;


            } 
            //De nuevo inicimos el contador 
            counter = 0;
            //Iniciamos otra varible para guardar la suma de todas las calificaciones
            double gradeSum = 0;
            //Usamos de nuevo un while para imprimir el resultado de todos los alumnos que pusimos en el primer while
            int noGrade = 0;
            while (counter < alumnCount)
            {
                if (names[counter]=="No capturado") { 
                    counter++;
                    noGrade++;
                    continue;

                }
                Console.WriteLine($"El alumno es {names[counter]} saco la calificacion {grades[counter]}, el alumno {(grades[counter] > fail ? "aprobo" : "reprobo")}");
                gradeSum += grades[counter];
                counter ++;

            }
            //Con esta operacion damos el promedio general del grupo
            double gradeAvg = gradeSum / (alumnCount-noGrade);

           

            Console.WriteLine($"El promedio del grupo es {gradeAvg}");
            Console.ReadKey();
        }
    }
}
