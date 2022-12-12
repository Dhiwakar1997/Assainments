#include <stdio.h>

#define SIZE 10

int arr[SIZE];
int front = -1, back = -1;

int isEmpty() {
  if (front == -1) return 1;
  return 0;
}

void enQueue(int data) {
    if (front == -1) 
    {
        front = 0;
    }
    back = (back + 1) % SIZE;
    arr[back] = data;
    printf("Enqueued item: %d\n",data);
}

int deQueue() {
  int data=arr[front];
    if (front == back) {
        front = -1;
        back = -1;
        } 
    else 
        front = (front + 1) % SIZE;
    printf("Dequeued item: %d\n",data);
    return (data);
}

void display() {
    printf("f-%d, b-%d\n",front,back);
    for (int i = front; i != back+1; i = (i + 1) % SIZE) 
      printf("%d\t", arr[i]);
    printf("\n");
}

int main() {

  enQueue(1);
  enQueue(2);
  enQueue(3);
  enQueue(4);
  enQueue(5);
  enQueue(6);

  display();
  deQueue();
  
  display();
  deQueue();
  display();

  enQueue(7);
  display();

  enQueue(8);
  display();
  
  return 0;
}