#include <stdio.h>
 
int main()
{
    FILE *file_pointer;
    char productName[20];
    int availableCount;
    float price;
 
    file_pointer = fopen("test_file.txt", "a");
 
    if (file_pointer == NULL)
    {
        printf("File does not exists \n");
        return 0;
    }
    printf("Quality = A1");
    fprintf(file_pointer, "Quality  = A1\n");
    fclose(file_pointer);
    return 0;
}