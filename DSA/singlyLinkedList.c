
#include <stdio.h>
#include <stdlib.h>

struct LinkedList{
int data;
struct LinkedList *next;
};

struct LinkedList *head=NULL;

void insertion(int data){
    struct LinkedList *temp = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    temp->data = data;
    temp->next = head;
    head = temp;
}

void deletion(int data){
        struct LinkedList *previous = head, *current = head->next;
        while(1){
            if(current->data == data){
                previous->next = current->next;
            }
        if (current->next==NULL)
        break;
        previous = current;
        current = current->next;
    }
}

void display(){
    struct LinkedList *temp = head;
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
deletion(3);
display();
}