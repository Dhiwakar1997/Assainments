#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(){
    int forkResult;
    printf("%d: I am the parent. Remember my number!\n", getpid());
    printf("%d: I am now going to fork ...\n",getpid());
    forkResult = fork();
    if(forkResult!=0){
        printf("%d: My child's pid is %d\n",getpid(), forkResult);

    }
    else{
        printf("%d: Hi! I am the child. \n",getpid());
    }
    printf("%d: like father like son. \n",getpid());
    return 0;
}