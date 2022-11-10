#include <stdio.h>
 
int main()
{
    FILE *file_pointer;
    char productName[20];
    int availableCount;
    float price;
 
    file_pointer = fopen("test_file.txt", "w");
 
    if (file_pointer == NULL)
    {
        printf("File does not exists \n");
        return 0;
    }
    printf("Enter the product name :\n");
    scanf("%s", productName);
    fprintf(file_pointer, "Product Name  = %s\n", productName);
    printf("Enter the available count :\n");
    scanf("%d", &availableCount);
    fprintf(file_pointer, "Available Count = %d\n", availableCount);
    printf("Enter the price of the product :\n");
    scanf("%f", &price);
    fprintf(file_pointer, "Price  = %.2f\n", price);
    fclose(file_pointer);
    return 0;
}