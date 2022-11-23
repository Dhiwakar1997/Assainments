#include <stdio.h>
#include <stdbool.h>

int arr[50], arrSize=-1,front=0,back=-1;

void enqueue(int data){
    arr[++back]= data;
    ++arrSize;
    printf("Enqueued item: %d\n",data);
}

int dequeue(){
    int temp = arr[front];
    arr[front]='\0';
    front++;
    printf("Dequeued item: %d\n",temp);
    return temp;
}

bool isEmpty()
{
return front == back||front ==-1;
}

int size(){
return arrSize;
}

void display(){
    for(int i=front;i<=back;i++)
        printf("%d\t",arr[i]);
    printf("\n");
}

int main() {
    enqueue(2);
    enqueue(5);
    enqueue(1);
    enqueue(7);
    display();
    dequeue();
    display();
    enqueue(8);
    display();
    return 0;
}