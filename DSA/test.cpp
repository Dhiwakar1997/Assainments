
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

class A
{
    public:
    int x;

};

A classFunc(){
    A a;
    a.x=56;
    return a;
}

int main()
{
    A g = classFunc();
    printf("%d\n",g.x);
}