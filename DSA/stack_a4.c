#include <stdio.h>
#include <stdbool.h>
int arr[50], arrSize=0, top=-1;

int pop(){
int temp = arr[top--];
arrSize--;
return temp;
}

void push(int data){
arr[++top]=data;
arrSize++;
}

bool isEmpty()
{
return top==-1;
}

int size(){
return arrSize;
}

void display(){
    for(int i=0;i<arrSize;i++)
        printf("%d\n",arr[i]);
}

int main() 
{
    push(2);
    push(4);
    push(1);
    push(8);
    printf("Popped item is %d\n",pop());
    push(3);
    display();
    return 0;
}