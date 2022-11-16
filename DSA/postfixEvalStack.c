#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

float arr[50], arrSize=0;
int top=-1;

float pop(){
float temp = arr[top--];
arrSize--;
return temp;
}

float charToFloat(char a){
    return a - 48.0;
}

char floatToChar(float a){
    return a+48.0;
}

void push(float data){
arr[++top]=data;
arrSize++;
}

bool isEmpty()
{
return top==-1;
}

int size(){
return arrSize;
}

void display(){
    for(int i=0;i<arrSize;i++)
        printf("%d: %f\n",i,arr[i]);
}

float eval(char operator)
{
    //printf("\nOperator: %c\n",operator);
    //display();

    float b = pop();
    float a = pop();
    if (operator=='+')
    {
    push(a + b);
    printf("\n%.2f + %.2f = %.2f\n",a,b,a+b);
    }

    else if (operator=='-')
    {
    push( a - b);
    printf("\n%.2f - %.2f = %.2f\n",a,b,a-b);
    }
    else if (operator=='/')
    {
    push( a / b);
    printf("\n%.2f/%.2f = %.2f\n",a,b,a/b);
    }

    else if (operator=='*')
    {
    push( a * b);
    printf("\n%.2f * %.2f = %.2f\n",a,b,a*b);
    }
    else if (operator=='^')
    {
    push(pow(a,b));
    printf("\n%.2f^%.2f = %.2f\n",a,b,pow(a,b));
    }

    return 0;
}

int isOperator(char x)
{
    if (x == '+'||x=='-'||x=='*'||x=='/'||x=='^')
    return 1;
    else
    return 0;
}

int main(){
int loopCount = 0;
char inputExp[30] = "9623-+*";
printf("\nPostfix Form: '%s'\n", inputExp);
int arrSize = sizeof(inputExp)/sizeof(inputExp[0]);
float out;
for(int i=0;i<arrSize;i++)
{
if(inputExp[i]==0)
break;
if (isOperator(inputExp[i])){
    out = eval(inputExp[i]);
}
else{
    push(charToFloat(inputExp[i]));
}
}

//display();
printf("\nPostfix expression '%s' evaluated result is %.2f\n", inputExp, pop());
return 0;
}