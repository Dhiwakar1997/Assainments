#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float interpolationFormula(int arr[], int x,int l, int u){
    float mid_part_num = x - arr[l], mid_part_denom = arr[u]-arr[l] ,mid_part;
    mid_part = round(mid_part_num/mid_part_denom);
    return l + mid_part * (u-l);
}

int main()
{
	int arr[] = { 4,17,22,30,41,52,55,61,66};
	int arr_size = sizeof(arr) / sizeof(arr[0]);
    int req=41, found=0, l=0, u = arr_size-1,loc;
    printf("Enter the element to be searched: \n");
    scanf("%d", &req);
    while(u-l>0){
        loc = interpolationFormula(arr, req, l, u);
        if(arr[loc]==req)
        {
            printf("Element %d is found at index %d\n",req,loc);
            found = 1;
            break;
        }
        //printf("l-%d, u-%d, loc-%d\n",l ,u ,loc);
        if (arr[loc]>req){
            u = loc -1;
        }
        else{
            l = l + 1;
        }
    }
    if(!found)
        printf("The element is not available in the array\n");
}