#include <sys/types.h>
#include <sys/dir.h>
#include <sys/param.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define FALSE 0
#define TRUE 1
extern  int alphasort();
#define GetCurrentDir getcwd

char pathname[FILENAME_MAX];

int file_select(struct dirent   *entry)
{
if ((strcmp(entry->d_name, ".") == 0) ||(strcmp(entry->d_name, "..") == 0))
return (FALSE);
else
return (TRUE);
}

int main()   {

int fileCount;
struct dirent **files;
int file_select();

GetCurrentDir( pathname, FILENAME_MAX );
printf("Current Working Directory = %s\n",pathname);
fileCount = scandir(pathname, &files, file_select, alphasort);
if (fileCount <= 0)
{         
printf("No files in this directory\n");
exit(0);
}
printf("Files count = %d\n",fileCount);
for (int i=1;i<fileCount ; i++)
{printf("  -%s \n",files[i-1]->d_name);}
return 0;
}