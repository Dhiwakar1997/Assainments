
#include <stdio.h>
#include <stdlib.h>


int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	int arr_size = sizeof(arr) / sizeof(arr[0]);
    int req, found=0;
    printf("Enter the element to be searched: \n");
    scanf("%d", &req);

    for(int i =0;i<arr_size;i++)
        if(arr[i]==req)
        {
            printf("The element %d is at index %d\n",req, i);
            found = 1;
        }

    if(!found)
    {
        printf("The element is not available in the array\n");
    }


}