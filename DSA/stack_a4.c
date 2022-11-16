#include <stdio.h>
#include <stdbool.h>
int arr[50], arrSize=0, top=-1;

int pop(){
int temp = arr[top--];
arrSize--;
printf("Popped item: %d\n",temp);
return temp;
}

void push(int data){
arr[++top]=data;
arrSize++;
printf("Pushed item: %d\n",data);
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
        printf("%d\t",arr[i]);
    printf("\n");
}

int main() 
{
    push(2);
    push(4);
    push(1);
    push(8);
    display();
    pop();
    display();
    push(3);
    display();
    return 0;
}