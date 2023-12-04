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

int is_char(char **matrix, int i, int j)
{
    return !(is_number(matrix, i, j) || matrix[i][j] == 46);
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

int main()
{
    FILE *file = open_file("input.txt");

    int lines = count_lines(file);
    int columns = count_columns(file);

    char **data = read_data(file, lines, columns);

    fclose(file);

    int total_sum = 0;

    for (int i = 0; i < lines; i++)
        for (int j = 0; j < columns; j++)
        {
            if (!is_number(data, i, j))
                continue;
            if (
                (i > 0 && j > 0 && is_char(data, i - 1, j - 1)) ||
                (i > 0 && is_char(data, i - 1, j)) ||
                (i > 0 && j < columns - 1 && is_char(data, i - 1, j + 1)) ||
                (j > 0 && is_char(data, i, j - 1)) ||
                (j < columns - 1 && is_char(data, i, j + 1)) ||
                (i < lines - 1 && j > 0 && is_char(data, i + 1, j - 1)) ||
                (i < lines - 1 && is_char(data, i + 1, j)) ||
                (i < lines - 1 && j < columns - 1 && is_char(data, i + 1, j + 1)))
            {
                int sum = 0, k = j;
                while (k < columns - 1 && is_number(data, i, k + 1))
                    k++;
                for (int pot = 0, l = k; k >= 0 && is_number(data, i, l); pot++, l--)
                {
                    sum += (data[i][l] - 48) * int_pow(10, pot);
                    data[i][l] = '.';
                }
                total_sum += sum;
            }
        }

    printf("Total sum: %d\n", total_sum);
}
