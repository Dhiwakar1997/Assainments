#include<stdio.h>
#include<ctype.h>

char stack[100];
int top = -1;

void push(char x)
{
    stack[++top] = x;
}

char pop()
{
    if(top == -1)
        return -1;
    else
        return stack[top--];
}

int priority(char x)
{
    if(x == '(')
        return 0;
    if(x == '+' || x == '-')
        return 1;
    if(x == '*' || x == '/')
        return 2;
    return 0;
}

int main()
{
    char exp[100];
    char *e, x;
    printf("Enter the expression : ");
    scanf("%s",exp);
    printf("\n");
    e = exp;
    char output[100];
    int out_idx=0, temp;
    
    while(*e != '\0')
    {
        if(isalnum(*e))
        {
            printf("%c ",*e);
            output[out_idx++] = *e;
        }
        else if(*e == '(')
            push(*e);
        else if(*e == ')')
        {
            while((x = pop()) != '(')
            {
            printf("%c ", x);
            output[out_idx++] = x;
            }
        }
        else
        {
            while(priority(stack[top]) >= priority(*e))
            {
                temp = pop();
                printf("%c ",temp);
                output[out_idx++] = temp;
            }
            push(*e);
        }
        e++;
    }
    
    while(top != -1)
    {
        temp = pop();
        printf("%c ",temp);
        output[out_idx++] = temp;
    }
    
        printf("\n");
    for(int i=0;i<out_idx;i++)
    printf("%c ",output[i]);
    printf("\n");
    return 0;

}