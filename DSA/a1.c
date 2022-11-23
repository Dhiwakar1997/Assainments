#include <stdio.h>

void deletion(int dynArray[], int *arrSize, int deletionIndex) {

    for(int i=deletionIndex; i<=*arrSize; i++)
        dynArray[i] = dynArray[i+1];
    *arrSize=*arrSize-1;

    printf("Deleted Index value %d\n",deletionIndex);
}

void insertion(int dynArray[], int *arrSize, int indexPosition) {
    int val;
    printf("Enter the value to be inserted in the index position '%d': ",indexPosition);
    scanf("%d",&val);

    for(int i=*arrSize; i>indexPosition; i--)
        dynArray[i] = dynArray[i-1];
    dynArray[indexPosition] = val;
    *arrSize=*arrSize+1;
    
    printf("Inserted value %d in index position %d\n", val, indexPosition);
}

void splitArr(int dynArray[], int *arrSize){

    int part1Size=*arrSize/2;
    
    printf("\nFirst half of the Array : \n");
    for(int i=0; i <part1Size;i++)
        printf("%d ",dynArray[i]);

    printf("\nSecond half of the Array : \n");
    for(int i=part1Size; i < *arrSize;i++)
        printf("%d ",dynArray[i]);
    printf("\n");
}

int main() {
    int A[20]={0,1,2,3,4,5,6,}, size=7;
    char B[20];

    printf("Please enter the number of elements: ");
    scanf("%d",&size);
    printf("Enter %d integer value for array A: \n",size);
    for(int i=0;i<size;i++)
    {
        scanf("%d",&A[i]);
    }
    printf("Enter value for string B: \n");
    scanf("%s",B);
    printf("The entered string is %s\n",B);

    deletion(A,&size,0);
    deletion(A,&size,size/2);
    deletion(A,&size,size);

    insertion(A,&size,0);
    insertion(A,&size,size/2);
    insertion(A,&size,size);

    splitArr(A,&size);

    
    return 0;
}