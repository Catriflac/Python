using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //PÉLDA BOLVASÁSOK
            
            /*
            string inputString;
            inputString = Console.ReadLine();

            int nOfItems;
            nOfItems = Convert.ToInt32(Console.ReadLine());
            */

            int[] nOfItems;
            nOfItems = Array.ConvertAll(Console.ReadLine().Split(' '),Convert.ToInt32);

            int szamlalo;
            int holtverseny;

            int[] scores = new int[nOfItems[0]];
            scores = Array.ConvertAll(Console.ReadLine().Split(' '),Convert.ToInt32);


            //MINTAKERESÉS
            for ( int i = 0 ; i < nOfItems[0] ; i++ )
            {
                szamlalo = 1;
                holtverseny = 1;

                for ( int j = 0 ; j < i ; j++ )
                {
                    if ( scores[j] > scores[i] )
                    {
                        szamlalo++;
                    }
                    else if ( scores[j] == scores[i] )
                    {
                        holtverseny++;
                    }
                }

                Console.WriteLine(szamlalo + " " + holtverseny);

            }

            //PÉLDA KIÍRÁS
            /*
            for (int i = 0 ; i < nOfItems.Length ; i++)
            {
                Console.Write(nOfItems[i] + " ");
            }
            */

        }
    }
}