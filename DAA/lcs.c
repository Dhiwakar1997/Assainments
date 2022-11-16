#include<stdio.h>
#include <string.h>

char string1[30]= "aabc", string2[30] = "abc", lcsStr[30];
int n1=4,n2=3;

struct lcs_node{
   int count;
   char out[30];
};

struct lcs_node maxi(struct lcs_node a, struct lcs_node b)
{

    if(a.count>b.count)
    {
       return a;
    }
    else
    {
       return b;
    }
}

struct lcs_node temp;

struct lcs_node LCS(int i, int j, char out)
{
    if(string1[i]=='\0'|| string2[j]=='\0')
    {
      temp.count = 0;
      return temp;
    }   
    if(string1[i]==string2[j])
    {
        temp.count +=1 ;
        strncat(temp.out, &string2[i],1);
        printf("count : %d, substring : %s, str1 : %c\n",temp.count,temp.out,string2[i]);
        return LCS(i+1,j+1,*temp.out);
    }   
    else
    { 
       return maxi(LCS(i+1,j,out),LCS(i,j+1,out));
    }   
}
int main()
{
    struct lcs_node output = LCS(0,0,'\0');
    return 0;
}