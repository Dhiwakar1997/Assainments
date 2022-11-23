
#include <stdio.h>
#include <stdlib.h>

void swap(int swappingArr[],int index_a, int index_b){
int temp = swappingArr[index_a];
swappingArr[index_a] = swappingArr[index_b];
swappingArr[index_b] = temp;
}

int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	int arr_size = sizeof(arr) / sizeof(arr[0]);
    for(int i=1; i<arr_size; i++){
        for(int j=i;j>=0;j--){
            if(arr[i]<arr[j]){
                swap(arr,i,j);
            }
        }
    }
}
