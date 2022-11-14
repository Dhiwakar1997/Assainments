#include <stdio.h>
#include <stdbool.h>

int arr[50], arrSize=-1,front=0,back=0;

void enqueue(int data){
    arr[++arrSize]= data;
}

int dequeue(){
    int temp = arr[0];
    for(int i=0; i<=arrSize; i++)
        arr[i] = arr[i+1];
    arr[arrSize]='\0';
    arrSize--;
    return temp;
}

bool isEmpty()
{
return arrSize==-1;
}

int size(){
return arrSize;
}

void display(){
    for(int i=0;i<=arrSize;i++)
        printf("%d\n",arr[i]);
}

int main() {
    enqueue(2);
    enqueue(5);
    enqueue(1);
    display();
    printf("Dequeued item : %d\n",dequeue());
    display();
    enqueue(8);

    return 0;
}