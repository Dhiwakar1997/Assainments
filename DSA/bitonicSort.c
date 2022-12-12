// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// void swap(int swappingArr[],int index_a, int index_b){
// int temp = swappingArr[index_a];
// swappingArr[index_a] = swappingArr[index_b];
// swappingArr[index_b] = temp;
// }

// void sort_ascending(int arr[],int a,int b){
// 	for(int i=a;i<=b;i++){
// 		for(int j=a;j<=b-i-1;j++){
// 			if(arr[j]>arr[j+1])
// 			{
// 			swap(arr,j,j+1);
// 			printf("swap : %d\t%d\n",arr[j],arr[j+1]);
// 			}		
// 		}
// 	}

// }

// void sort_descending(int arr[],int a,int b){
// 	printf("descending started %d to %d\n",a,b);
// 	for(int i=a;i<=b;i++)
// 	{
// 		printf("i=%d\t\n",i);
// 		for(int j=a;j<=b-i-1;j++){
// 					printf("j=%d\t\n",j);
// 			printf("%d\t%d\n",arr[j],arr[j+1]);
// 			if(arr[j]>arr[j+1])
// 			{
// 			swap(arr,j,j+1);
// 			printf("swap : %d\t%d\n",arr[j],arr[j+1]);
// 			}
// 		}
// 	}
// }

// void display(int arr[],int arrSize){
//     for(int i=0;i<arrSize;i++){
//         printf("%d\t",arr[i]);
//         }
//         printf("\n\n");
//     }

// int main()
// {
// 	int arr[] = { 25,15,72,82,92,1,7,62};

// 	double arr_size = sizeof(arr) / sizeof(arr[0]);
// 		sort_descending(arr,4,7);
// 		display(arr,arr_size);
// 	double partition =  log2( arr_size ) -1;
// 	for(int i=1;i<=partition;i++){
// 		int current_partition = pow(2,i);
// 		int sort_order_flag =0;
// 		for(int j=0;j<=arr_size;j=j+current_partition)
// 		{
// 			display(arr,arr_size);
// 			if(sort_order_flag%2==0){
				
// 				printf("Ascending: %d\t%d\n",j,j+current_partition-1);
// 				sort_ascending(arr,j,j+current_partition-1);

// 			}
// 			else{
// 				printf("Descending: %d\t%d\n",j,j+current_partition-1);
// 				sort_descending(arr,j,j+current_partition-1);
// 			}
// 			sort_order_flag++;
// 			display(arr,arr_size);
// 		}
// 	}
// 	display(arr,arr_size);
// }


#include<stdio.h>    

void exchange(int a[], int i, int j, int d)    
{    
    int temp;    
    if (d==(a[i]>a[j]))    
    {    
        temp = a[i];    
        a[i] = a[j];    
        a[j] = temp;    
    }    
}    
void merge(int a[], int beg, int c, int d)    
{    
    int k, i;    
    if (c > 1)    
    {    
        k = c/2;    
        for (i = beg; i < beg+k; i++)    
            exchange(a, i, i+k, d);    
        merge(a, beg, k, d);    
        merge(a, beg+k, k, d);    
    }    
}    

void bitonicSort(int a[],int beg, int c, int d)    
{    
    int k;    
    if (c>1)    
    {    
        k = c/2;    
        bitonicSort(a, beg, k, 1);  
        bitonicSort(a, beg+k, k, 0);   
        merge(a,beg, c, d);   
    }    
}    
     

void sort(int a[], int n, int order)    
{    
    bitonicSort(a, 0, n, order);    
}    

 void print(int a[], int n) 
    {  
    int i;  
    for(i = 0; i < n; i++)    
    {    
        printf("%d ",a[i]);    
    }        
    }  
  
int main()    
{    
    int a[]= {30, 70, 40, 80, 60, 20, 10, 50};    
    int n = sizeof(a)/sizeof(a[0]);   
    int order = 1;  
    printf("Before sorting array elements are - \n");  
    print(a, n);  
    sort(a, n, order);    
    printf("\nAfter sorting array elements are - \n");    
    print(a, n); 
	printf("\n");
    return 0;  
}   
