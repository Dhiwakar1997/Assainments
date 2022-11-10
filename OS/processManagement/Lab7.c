#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
int main(){
    int pid;
    pid = fork();
    if(pid!=0)
    {
        while(1);
        sleep(10);
    }
    else{
        exit(1);
    }
    return 0;
}