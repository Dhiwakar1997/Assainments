
#include <stdio.h>
#include <stdlib.h>

void swap(int swappingArr[],int index_a, int index_b){
int temp = swappingArr[index_a];
swappingArr[index_a] = swappingArr[index_b];
swappingArr[index_b] = temp;
}

void display(int arr[],int arrSize){
    for(int i=0;i<arrSize;i++){
        printf("%d\t",arr[i]);
        }
        printf("\n\n");
    }

int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	int arr_size = sizeof(arr) / sizeof(arr[0]);
    printf("\nThe unsorted input is: \n\n");
    display(arr, arr_size);
    for(int i=1; i<arr_size; i++){
        int temp_swap=i;
        for(int j=i-1;j>=0;j--){
            if(arr[j]>arr[temp_swap]){
                swap(arr,temp_swap,j);
                display(arr, arr_size);
                temp_swap--;
            }
            else{
                break;
            }
        }
    }
printf("The sorted output is: \n\n");
display(arr, arr_size);
}
