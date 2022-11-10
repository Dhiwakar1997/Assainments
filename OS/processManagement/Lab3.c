//MultiForking
#include <stdio.h>
#include <unistd.h>

int main(){
    printf("Here i am just before the first forking statement\n");
    fork();
    printf("Here i am just after the first forking statement\n");
    fork();
    printf("Here i am just after the second forking statement\n");
    printf("\t I am process %d.\n", getpid());
    return 0;
}