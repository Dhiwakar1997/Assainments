#include <stdio.h>
#include <stdbool.h>

int arr[50], arrSize=-1,front=0,back=-1;

void enqueue(int data){
    arr[++back]= data;
    ++arrSize;
}

int dequeue(){
    int temp = arr[front];
    arr[front]='\0';
    front++;
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
        printf("%d\n",arr[i]);
}

int main() {
    enqueue(2);
    enqueue(5);
    enqueue(1);
    enqueue(7);
    printf("%d, %d\n",front,back);
    display();
    printf("Dequeued item : %d\n",dequeue());
    display();
    enqueue(8);

    return 0;
}