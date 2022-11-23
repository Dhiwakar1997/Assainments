
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct DoublyLinkedList{
    int data;
    struct DoublyLinkedList *prev;
    struct DoublyLinkedList *next;
};

struct DoublyLinkedList *head=NULL;
struct DoublyLinkedList *tail=NULL;

bool isEmpty(){
    return head==NULL && tail==NULL;
}

void insertion(int data){
    struct DoublyLinkedList *temp = (struct DoublyLinkedList*)malloc(sizeof(struct DoublyLinkedList));
    head->prev = temp;
    temp->data = data;

       if(isEmpty()) {
      //make it the last link
      tail = temp;
   } else {
      //update first prev link
      head->prev = temp;
   }
    temp->next = head;
    head = temp;
}

void deletion(int data){
    struct DoublyLinkedList *current = head;
        printf("yet to enter!");
        while(1){
            printf("%d\t",current->data);
            if(current->data == data){
                struct DoublyLinkedList *prev = current->prev;
                printf("%p\n",prev);
               // prev->next = current->next;
                //current = NULL;
                break;
            }
            if (current->next==NULL)
                break;
            current = current->next;
        }
}

void display(){
    struct DoublyLinkedList *temp = head;
    while(1){
        printf("%d\t", temp->data);
        if (temp->next==NULL)
        break;
        temp = temp->next;
    }
    printf("\n");
}

int main()
{
insertion(23);
insertion(3);
insertion(2);
insertion(8);
display();
printf("%d\n",head->data);
deletion(3);
display();
}