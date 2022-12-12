#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int arr[] = { 4,17,22,30,41,52,55,61,66};
	int arr_size = sizeof(arr) / sizeof(arr[0]);
    int req=41, found=0, i=1, u = arr_size-1,loc;
    printf("Enter the element to be searched: \n");
    scanf("%d", &req);
    if(arr[0]==req)
        {    
        loc = 0;    
        found=1;
        }
    while(!found){
        if(arr[i]==req)
        {
            loc = i;
            found = 1;
            break;
        }
        else if ( arr[i]<req)
        {
            i=i*2;
        }
    }
    if(!found)
        printf("The element is not available in the array\n");
}