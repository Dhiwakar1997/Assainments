
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
        printf("\n");
    }

int main()
{
	int arr[7] = { 12, 1, 11, 13, 5, 6, 7 };
	int arr_size = 7;//sizeof(arr) / sizeof(arr[0]);
    int tail = arr_size;
    for(int head = 0;head<arr_size/2;head++)
    {
        
        for(int i = head;i< tail;i++){
            if(arr[i]>arr[i+1]){
                swap(arr,i,i+1);
            }
        }
        printf("After forward swap:\n");
        display(arr, arr_size);
        tail--;

        for(int i = tail;i> head;i--){
            if(arr[i]<arr[i-1]){
                swap(arr,i,i-1);
            }
        }
        printf("Backward forward swap:\n");
        display(arr, arr_size);
    }
    printf("\n\nFinal Output:\n");
    display(arr, arr_size);

}
