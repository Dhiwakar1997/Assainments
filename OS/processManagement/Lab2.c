#include <stdio.h>
#include <unistd.h>

int main(){
    int pid;
    printf("Hello World\n");
    printf("I am parent process and my pid is %d\n",getpid());
    printf("Here i am before the forking\n");
    pid = fork();
    printf("Here i am after the forking\n");
    if(pid==0){
        printf("I am the child process, my process id is %d\n",getpid());
    }
    else{
        printf("I am the process, my process id is %d\n",getpid());
    }
    return 0;
}