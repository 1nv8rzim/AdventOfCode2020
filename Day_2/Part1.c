#include <stdio.h>
#include <stdlib.h>

int count(char str[32], char letter);

int main()
{

    FILE *file;
    file = fopen("input.txt", "r");

    //read file into array
    char range[1000][6];
    char letter[1000][4];
    char password[1000][32];
    int i;

    if (file == NULL)
    {
        printf("Error Reading File\n");
        exit(0);
    }

    for (i = 0; i < 1000; i++)
    {
        fscanf(file, "%s", range[i]);
        fscanf(file, "%s", letter[i]);
        fscanf(file, "%s", password[i]);
    }

    char low[1000][3];
    char high[1000][3];
    char temp[2];

    for (i = 0; i < 1000; i++)
    {
        if (range[i][1] == '-')
        {
            low[i][0] = range[i][0];
            if (range[i][3] == '\0')
            {
                high[i][0] = range[i][2];
            }
            else
            {
                high[i][0] = range[i][2];
                high[i][1] = range[i][3];
            }
        }
        else
        {
            low[i][0] = range[i][0];
            low[i][1] = range[i][1];
            if (range[i][4] == '\0')
            {
                high[i][0] = range[i][3];
            }
            else
            {
                high[i][0] = range[i][3];
                high[i][1] = range[i][4];
            }
        }
    }

    int nums[1000][2];

    for (i = 0; i < 1000; i++)
    {
        nums[i][0] = atoi(low[i]);
        nums[i][1] = atoi(high[i]);
    }
    int num = 0;

    for (i = 0; i < 1000; i++)
    {
        if (nums[i][0] <= count(password[i], letter[i][0]) && count(password[i], letter[i][0]) <= nums[i][1])
        {
            num++;
        }
    }

    printf("%d\n", num);
}

int count(char str[32], char letter)
{
    int num = 0;

    for (int i = 0; i < 32; i++)
    {
        if (str[i] == letter)
        {
            num++;
        }
    }

    return num;
}