
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
	int arr[] = { 56, 8, 13, 32, 0, -7 };
	int arr_size = sizeof(arr) / sizeof(arr[0]);
    printf("\nThe unsorted input is: \n\n");
    display(arr,arr_size);
    printf("\n");
    for(int i=0;i<arr_size;i++){
        int smallest_index=i;
        for(int j=i+1;j<arr_size;j++){
            if(arr[j]<arr[smallest_index])
            smallest_index = j;
        }
    swap(arr,i,smallest_index);
    display(arr,arr_size);
    }
printf("\nThe sorted output is: \n\n");
display(arr,arr_size);
}
