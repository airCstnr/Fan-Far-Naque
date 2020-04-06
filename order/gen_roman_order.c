/*
 * Generate JSON file containing roman numbering order
 * 
 * Original Author : Timothée Goetschy
 * Author : Raphaël Castanier
 * 
 * 2020
 * 
 */

#include <stdlib.h>
#include <stdio.h>

int main (int argc, char *argv[])
{
    char* i = "\"i\"";  // 1
    char* v = "\"v\"";  // 5
    char* x = "\"x\"";  // 10
    char* l = "\"l\"";  // 50
    char* c = "\"c\"";  // 100
    char* d = "\"d\"";  // 500
    char* m = "\"m\"";  // 1000

    int maxNumber = 5000;

    int loopNumber;
    FILE *fichier = NULL;
    fichier = fopen("order.json", "w+");


    // start filling file
    fprintf(fichier, "{\"order\":[\n");
    for (int n = 1 ; n <= maxNumber ; n ++)
    {
        loopNumber = n;
        while (0 < loopNumber)
        {            
            if (loopNumber <= 3)
            {
                for (int j = 0 ; j < loopNumber ; j ++)
                {
                    fprintf(fichier, "[%s, %d],\n", i, n);
                }
                loopNumber = 0;
            }
            else if (loopNumber == 4)
            {
                fprintf(fichier, "[%s, %d],\n", i, n);
                fprintf(fichier, "[%s, %d],\n", v, n);
                loopNumber = 0;
            }
            else if (loopNumber == 9)
            {
                fprintf(fichier, "[%s, %d],\n", i, n);
                fprintf(fichier, "[%s, %d],\n", x, n);
                loopNumber = 0;
            }

            else if (1000 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", m, n);
                loopNumber -= 1000;
            }
            else if (900 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", c, n);
                fprintf(fichier, "[%s, %d],\n", m, n);
                loopNumber -= 900;
            }
            else if (500 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", d, n);
                loopNumber -= 500;
            }
            else if (400 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", c, n);
                fprintf(fichier, "[%s, %d],\n", d, n);
                loopNumber -= 400;
            }
            else if (100 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", c, n);
                loopNumber -= 100;
            }
            else if (90 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", x, n);
                fprintf(fichier, "[%s, %d],\n", c, n);
                loopNumber -= 90;
            }
            else if (50 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", l, n);
                loopNumber -= 50;
            }
            else if (40 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", x, n);
                fprintf(fichier, "[%s, %d],\n", l, n);
                loopNumber -= 40;
            }
            else if (10 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", x, n);
                loopNumber -= 10;
            }
            else if (5 <= loopNumber)
            {
                fprintf(fichier, "[%s, %d],\n", v, n);
                loopNumber -= 5;
            }
        }
    }
    
    // add a trailing element
    fprintf(fichier, "[\"END\", -1]\n");
    
    // close Json dict
    fprintf(fichier, "]}\n");
    
    fclose(fichier);

    return EXIT_SUCCESS;
}
 
