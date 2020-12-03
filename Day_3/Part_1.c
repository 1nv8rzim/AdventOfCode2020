#include <stdio.h>
#include <stdlib.h>

int count_trees(char area[323][64], int x_step, int y_step);

int main()
{
    FILE *file;
    file = fopen("input.txt", "r");

    //read file into array
    char area[323][64];
    int i;

    if (file == NULL)
    {
        printf("Error Reading File\n");
        exit(0);
    }

    for (i = 0; i < 323; i++)
    {
        fscanf(file, "%s", area[i]);
    }

    int num;

    num = count_trees(area, 3, 1);

    printf("%d\n", num);
}

int count_trees(char area[323][64], int x_step, int y_step)
{
    int num = 0;
    int mod = 31;
    int x = 0;
    int y = 0;
    for (int i = 0; i < 323; i++)
    {
        if (area[y][x] == '#')
        {
            num++;
        }
        x = (x + x_step) % mod;
        y = y + y_step;
    }
    return num;
}