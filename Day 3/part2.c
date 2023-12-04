#include <stdio.h>
#include <stdlib.h>

FILE *open_file(char *path)
{
    FILE *file = fopen(path, "r");
    if (file == NULL)
    {
        printf("Error opening file\n");
        exit(1);
    }
    return file;
}

int count_lines(FILE *file)
{
    rewind(file);
    int lines = 1;
    while (fscanf(file, "%*[^\n]%*c") != EOF)
        lines++;
    return lines;
}

int count_columns(FILE *file)
{
    rewind(file);
    int columns = 0;
    char ch;
    while (1)
    {
        fscanf(file, "%c", &ch);
        if (ch == '\n')
            break;
        columns++;
    }
    return columns;
}

char **init_matrix(int lines, int columns)
{
    char **matrix = (char **)malloc(lines * sizeof(char *));
    if (matrix == NULL)
    {
        printf("Error allocating memory\n");
        exit(1);
    }
    for (int i = 0; i < lines; i++)
    {
        matrix[i] = (char *)malloc(columns * sizeof(char));
        if (matrix[i] == NULL)
        {
            printf("Error allocating memory\n");
            exit(1);
        }
    }
    return matrix;
}

char **read_data(FILE *file, int lines, int columns)
{
    rewind(file);
    char **matrix = init_matrix(lines, columns);
    char ch;
    for (int i = 0; i < lines; i++)
    {
        for (int j = 0; j < columns; j++)
            fscanf(file, "%c", &matrix[i][j]);
        fscanf(file, "%c", &ch);
    }
    return matrix;
}

void print_matrix(char **matrix, int lines, int columns)
{
    printf("\n");
    for (int i = 0; i < lines; i++)
    {
        for (int j = 0; j < columns; j++)
            printf("%c", matrix[i][j]);
        printf("\n");
    }
}

int is_number(char **matrix, int i, int j)
{
    return matrix[i][j] >= 48 && matrix[i][j] <= 57;
}

int int_pow(int base, int exp)
{
    int result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }
    return result;
}

int sum_position_if_valid(char **matrix, int columns, int k, int l)
{
    if (is_number(matrix, l, k))
    {
        int sum = 0, pot = 0;
        while (k < columns - 1 && (matrix[l][k + 1] >= 48 && matrix[l][k + 1] <= 57))
            k++;
        while (k >= 0 && (matrix[l][k] >= 48 && matrix[l][k] <= 57))
        {
            sum += (matrix[l][k] - 48) * int_pow(10, pot);
            matrix[l][k] = '.';
            pot++;
            k--;
        }
        return sum;
    }
    return -1;
}

int main()
{
    FILE *file = open_file("input.txt");

    int lines = count_lines(file);
    int columns = count_columns(file);

    char **data = read_data(file, lines, columns);

    fclose(file);

    int total_ratio_sum = 0, ratio;

    for (int i = 0; i < lines; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            int matches = 0, res;
            ratio = 1;
            if (data[i][j] != '*')
                continue;
            if (i > 0 && j > 0)
            {
                res = sum_position_if_valid(data, columns, j - 1, i - 1);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (i > 0)
            {
                res = sum_position_if_valid(data, columns, j, i - 1);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (i > 0 && j < columns - 1)
            {
                res = sum_position_if_valid(data, columns, j + 1, i - 1);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (j > 0)
            {
                res = sum_position_if_valid(data, columns, j - 1, i);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (j < columns - 1)
            {
                res = sum_position_if_valid(data, columns, j + 1, i);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (i < lines - 1 && j > 0)
            {
                res = sum_position_if_valid(data, columns, j - 1, i + 1);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (i < lines - 1)
            {
                res = sum_position_if_valid(data, columns, j, i + 1);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (i < lines - 1 && j < columns - 1)
            {
                res = sum_position_if_valid(data, columns, j + 1, i + 1);
                if (res > -1)
                {
                    ratio *= res;
                    matches++;
                }
            }
            if (matches == 2)
                total_ratio_sum += ratio;
        }
    }

    printf("Total ratio: %d\n", total_ratio_sum);
}
