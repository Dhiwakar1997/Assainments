#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

char postfixExpression[6] = "963+*";

float eval(float a, float b, char operator)
{
    //printf("Operator: %c\n",operator);
    if (operator=='+')
    return a + b;
    else if (operator=='-')
    return a - b;
    else if (operator=='/')
    return a / b;
    else if (operator=='*')
    return a * b;
    else if (operator=='^')
    return pow(a,b);

    return 0;
}

int isOperator(char x)
{
    if (x == '+'||x=='-'||x=='*'||x=='/'||x=='^')
    return 1;
    else
    return 0;
}

float charToFloat(char a){
    return a - 48.0;
}

char floatToChar(float a){
    return a+48.0;
}

void deletion(char dynArray[], int *arrSize, int deletionIndex) {
    for(int i=deletionIndex; i<=*arrSize; i++)
        dynArray[i] = dynArray[i+1];
    dynArray[*arrSize]='\0';
   *arrSize = *arrSize-1;
    //printf("Deleted Index value %d\n",deletionIndex);
}

void insertion(char dynArray[], int *arrSize, int indexPosition, char item) {

    for(int i=*arrSize; i>indexPosition; i--)
        dynArray[i] = dynArray[i-1];
    dynArray[indexPosition] = item;
    *arrSize = *arrSize+1;
   // printf("Inserted value %d in index position %d\n", item, indexPosition);
}

int main(){
int loopCount = 0;
char inputExp[6] = "963+*";
float out;
int arrSize = sizeof(postfixExpression)/sizeof(postfixExpression[0]);
while(1){
if (isOperator(postfixExpression[loopCount])){
    float a = charToFloat(postfixExpression[loopCount-2]);
    float b =charToFloat(postfixExpression[loopCount-1]);

    char operator = postfixExpression[loopCount];
    out = eval(a,b,operator);
    //printf("out : %f\n", out);

    deletion(postfixExpression,&arrSize,loopCount);
    deletion(postfixExpression,&arrSize,loopCount-1);
    deletion(postfixExpression,&arrSize,loopCount-2);

    insertion(postfixExpression,&arrSize,loopCount-2,floatToChar(out));
    loopCount-=2;

}
loopCount++;

int endFlag = 0;

for(int i=0;i<arrSize;i++)
    if(isOperator(postfixExpression[i]))
        endFlag = 1;
//printf("size of string: %d\n", arrSize);

if(endFlag==0)
break;
}
printf("Postfix expression '%s' evaluated result is %.2f\n", inputExp, out);
return 0;
}