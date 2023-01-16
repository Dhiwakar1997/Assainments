#include<stdio.h>
#include<mpi.h>
int main()
{
 MPI_Init(NULL, NULL);
 int rank;
 float num_1=25, num_2=38;
 MPI_Comm_rank(MPI_COMM_WORLD, &rank);
 
 if(rank==0)
 {

 printf("Division of num_1 and num_2: %.2f\n",num_1/num_2);
 
 }
 if(rank==1)
 {

 printf("Multiplication of num_1 and num_2: %.2f\n",num_1*num_2);
 
 }

  if(rank==2)
 {

 printf("Subtraction of num_1 and num_2: %.2f\n",num_1-num_2);
 
 }

  if(rank==3)
 {

 printf("Addision of num_1 and num_2: %.2f\n",num_1+num_2);
 
 }

 MPI_Finalize();
 return 0;
}