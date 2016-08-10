using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AGeo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Název souboru:");
            string name = Console.ReadLine();

            Files f = new Files();
            f.create(name);

            Console.WriteLine("Zadej položky do listu");

            List<string> s = new List<string>();
            ConsoleKeyInfo cki = new ConsoleKeyInfo('E', ConsoleKey.E, false, false, false);
            while (cki.Key != ConsoleKey.Escape)

                // Bug s entrem na první řádce?
            {
                Console.WriteLine("---------------------------------------------");
                Console.Write("Další položkou je: ");
                s.Add(Console.ReadLine().ToString());
                Console.Write("Pro zadání další hodnoty stiskni libovolnou klávesu, pro ukončení stiskni Escape");
                cki = Console.ReadKey();
            }


            f.addList(s);
            s.ForEach(delegate (string value)
            {
                Console.WriteLine(value);
            });
            Console.Write(f);


            Console.ReadKey();
        }
    }
}
