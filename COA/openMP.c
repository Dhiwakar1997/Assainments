//#include<stdio.h>
//#include<omp.h>
//int main(void)
//{
//int threadCount,threadNum,processCount,maxThread;
//printf("hello world\n");
//    omp_set_num_threads(3);
//#pragma omp parallel
//{
//
//threadCount=omp_get_num_threads();
//threadNum=omp_get_thread_num();
//processCount=omp_get_num_procs();
//maxThread=omp_get_max_threads();
//    printf("\nNumber of threads : %d", threadCount);
//    printf("\nThread number : %d", threadNum);
//    printf("\nNumber of processors : %d", processCount);
//    printf("\nMaximum threads : %d\n", maxThread);
//
//}
//
//    return 0;
//}
//#include<stdio.h>
//#include<omp.h>
//void main()
//{
//    int tid;
//    float input1=10,input2=12;
//    double startTime, endTime, timeTaken;
//    omp_set_num_threads(4);
//#pragma omp parallel
//    {
//
//        tid = omp_get_thread_num();
//        printf("tid: %d\n",tid);
//        startTime=omp_get_wtime();
//        if(tid==0)
//        {
//            printf("Addition of %.2f and %.2f is %.2f\n",input1,input2,input1+input2);
//        }
//        else if(tid==1)
//        {
//
//            printf("Subtraction of %.2f and %.2f is %.2f\n",input1,input2,input1-input2);
//        }
//        else if(tid==2)
//        {
//            printf("Multiplication of %.2f and %.2f is %.2f\n",input1,input2,input1*input2);
//        }
//        else if(tid==3)
//        {
//            printf("Division of %.2f and %.2f is %.2f\n",input1,input2, input1/input2);
//        }
//        endTime=omp_get_wtime();
//        timeTaken = endTime - startTime;
//        printf("the measured time is: %lf\n", timeTaken);
//    }
//}

//#include<stdio.h>
//#include <time.h>
//int main(void)
//{
//
//    clock_t tempTime;
//    tempTime = clock();
//    int arr[3] = {32,25,87},min,max;
//    min = arr[0];
//    max = arr[0];
//    for(int i=1; i < 3;i++){
//        if(arr[i]<min){
//            min = arr[i];
//        }
//    }
//    for(int i=1; i < 3;i++){
//        if(arr[i]>max){
//            max = arr[i];
//        }
//    }
//    printf("The maximum number is %d\n",max);
//    printf("The minimum number is %d\n",min);
//    tempTime = clock() - tempTime;
//    double timeTaken = ((double)tempTime)/CLOCKS_PER_SEC;
//    printf("Total time taken is %f\n", timeTaken);
//
//    return 0;
//}

//
//#include<stdio.h>
//#include <omp.h>
//int main(void)
//{
//int s=44, p=34, fp=87, lp=3;
//omp_set_num_threads(1);
//
//#pragma omp parallel shared(s) private(p) firstprivate(fp)
//    {
//
//        printf("shared variable s is %d\n",s);
//        printf("firstprivate variable fp is %d\n",fp);
//        printf("private variable p before assaiments inside thread is %d\n",p);
//        p = 34;
//        printf("private variable p after assaiments inside thread is %d\n",p);
//        lp++;
//    }
//
//    return 0;
//}

//#include <stdio.h>
//#include <stdlib.h>
//#include <omp.h>
//int main(void)
//{
//int i;
//int x;
//x=44;
//#pragma omp parallel for lastprivate(x)
//for(i=0;i<=10;i++)
//{
//x=i;
//printf("Thread number: %d x: %d\n",omp_get_thread_num(),x);
//}
//printf("x is %d\n", x);
//}

#include<stdio.h>
#include <omp.h>
int a, b, i, tid;
float x;
#pragma omp threadprivate(a, x)
void main ()
{

omp_set_dynamic(0);

printf("First Parallel Region:\n");
#pragma omp parallel private(b,tid)
{
tid = omp_get_thread_num();
a = tid;
b = tid;
x = 1.1 * tid +1.0;
printf("Thread %d: a,b,x= %d %d %f\n",tid,a,b,x);
}


printf("Master thread\n");

printf("Second Parallel Region:\n");
#pragma omp parallel private(tid)
{
tid = omp_get_thread_num();
printf("Thread %d: a,b,x= %d %d %f\n",tid,a,b,x);
}

}
