#include <stdio.h>
#include <unistd.h>

int main(){
    printf("Hello World");
    fork();
    printf("I am after the fork\n");
    printf("\t I am process %d.\n", getpid());
    return 0;
}