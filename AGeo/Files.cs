using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace AGeo
{
    class Files
    {
        protected string name { get; set; }
        /// <summary>
        /// 
        /// </summary>
        public Files()
        {
            this.name = "";
            try
            {
                Directory.CreateDirectory("Save");
            }
            catch
            {
                Console.WriteLine("Složka Save již existuje");
            }
        }
        /// <summary>
        /// 
        /// </summary>
        /// <param name="name"></param>
        public void create(string name)
        {
            this.name = String.Format("Save/{0}.txt", name);
            try
            {
                File.CreateText(String.Format(name)).Close();
            }
            catch
            {
                Console.WriteLine("Při vytváření souboru došlo k chybě");

            }
        }
        /// <summary>
        /// Zapíše list do daného souboru
        /// </summary>
        /// <param name="list">List hodnot (string)</param>
        public void addList(List<string> list)
        {
            File.AppendAllLines(name, list);
        }
        /// <summary>
        /// 
        /// </summary>
        /// <returns></returns>
        public override string ToString()
        {
            return (String.Format("Name of created file is {0}", name));
        }
    }
}
