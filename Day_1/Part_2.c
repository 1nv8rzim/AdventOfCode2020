
#include <stdio.h>
#include <stdlib.h>

int main()
{

    FILE *file;
    file = fopen("input.txt", "r");

    //read file into array
    int data[200];
    int i;

    if (file == NULL)
    {
        printf("Error Reading File\n");
        exit(0);
    }

    for (i = 0; i < 200; i++)
    {
        fscanf(file, "%d,", &data[i]);
    }

    for (i = 0; i < 199; i++)
    {
        for (int j = i + 1; j < 200; j++)
        {
            for (int k = j + 1; k <= 200; k++)
            {
                if (data[i] + data[j] + data[k] == 2020)
                {
                    printf("%d * %d * %d = %d", data[i], data[j], data[k], data[i] * data[j] * data[k]);
                }
            }
        }
    }

    fclose(file);

    return 0;
}
