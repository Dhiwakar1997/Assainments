#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(){
int pid, status;
printf("\nHello World");
if (pid==-1){
   perror("\nbad fork");
   exit(1); 
}
else if (pid==0){
    printf("\nI am the child process");
}
else{
    wait(&status);
    printf("\nI am the parent process");
}
    return 0;
}