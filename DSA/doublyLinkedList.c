#include <stdio.h>
#include <stdlib.h>


struct Node {
  int data;
  struct Node* next;
  struct Node* prev;
};


void insertFront(struct Node** head, int data) {

  struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  newNode->next = (*head);
  newNode->prev = NULL;

  if ((*head) != NULL)
    (*head)->prev = newNode;
  (*head) = newNode;

}

void deleteNode(struct Node** head, struct Node* del_node) {
  if (*head == NULL || del_node == NULL)
    return;

  if (*head == del_node)
    *head = del_node->next;
  if (del_node->next != NULL)
    del_node->next->prev = del_node->prev;

  if (del_node->prev != NULL)
    del_node->prev->next = del_node->next;
  free(del_node);
}

void displayList(struct Node* node) {
  struct Node* last;

  while (node != NULL) {
    printf("%d->", node->data);
    last = node;
    node = node->next;
  }
  if (node == NULL)
    printf("NULL\n");
}

int main() {

  struct Node* head = NULL;


  insertFront(&head, 1);
  insertFront(&head, 6);
  insertFront(&head, 54);
  insertFront(&head, 9);
  displayList(head);

  deleteNode(&head, head->next);

  displayList(head);
}