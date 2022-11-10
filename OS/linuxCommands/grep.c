#include <stdio.h>
#include <stdlib.h>
#include<dirent.h>
#include<conio.h>
#define DATA_SIZE 1000
#define BUFFER_SIZE 1000
void countch(){
  FILE *fptr;
    char path[100];

    char word[50];

    int wCount;



    printf("Enter file name: ");
    scanf("%s", path);


    printf("Enter word to search in file: ");
    scanf("%s", word);
    fptr = fopen(path, "r");


    if (fptr == NULL)
    {
 printf("Unable to open file.\n");
 printf("Please check you have read/write previleges.\n");

 exit(EXIT_FAILURE);
    }


    Search_in_File(fptr, word);
    printf("%d",wCount);
    fclose(fptr);

}

int Search_in_File(char *fname, char *str)
{
 FILE *fp;
 int line_num = 1;
 int find_result = 0;
 char temp[512];
  if((fopen(fname, "r")) != NULL) {
  return(-1);
 }

 while(fgets(temp, 512, fp) != NULL) {
  if((strstr(temp,str)) != NULL) {
       
   line_num=line_num+0;
   printf("\n%s\n", temp);
   find_result++;
  }
  line_num++;
 }

if(find_result == 0) {
 printf("\nSorry, couldn't find a match.\n");
 }


 if(fp) {
  fclose(fp);
 }
 return(0);
}

int main(){
 countch();
 getch();
 return 0;
}