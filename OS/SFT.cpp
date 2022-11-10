#include<iostream>

using namespace std;

int main()
{
    int processCount, currentTime=0;
    float avgWaitingTime,avgTurnAroundTime,waitingTime=0,turnAroundTime=0;
    cout<< "Enter the number of Processes: ";
    cin>> processCount;
    int burstTime[processCount], arraivalTime[processCount]
    ,completionTime[processCount], processOrder[processCount];
    
    
    for(int i=0;i<processCount;i++){
        cin>>burstTime[i];
        arraivalTime[i]=0;
        processOrder[i]=i;
    }
    
    for(int i=0;i<processCount;i++){
    int noChange=1;
    for(int j=i+1;j<processCount;j++){
        if(burstTime[i]>burstTime[j]){
            noChange=0;
            int temp;
            temp = processOrder[j];
            processOrder[j] = processOrder[i];
            processOrder[i] =temp;
            temp = burstTime[j];
            burstTime[j] = burstTime[i];
            burstTime[i]=temp; }} }
    
    for(int i=0;i<processCount;i++){
        cout<<"\nBT-"<<burstTime[i];
        cout<<" PO-"<<processOrder[i];
    }
    
    for(int i=0;i<processCount;i++)
    {
        currentTime += burstTime[i];
        completionTime[i]=currentTime;
        turnAroundTime+=completionTime[i]-arraivalTime[i];
        if(i==0)continue;
        waitingTime+=completionTime[i-1]-arraivalTime[i-1];
    }    
    
    avgWaitingTime=waitingTime/processCount;
    avgTurnAroundTime=turnAroundTime/processCount;
    cout<<"\nThe Total Waiting time is : "<<waitingTime;
    cout<<"\nThe average Waiting time is : "<<avgWaitingTime;
    cout<<"\nThe Total Turn Around time is : "<<turnAroundTime;
    cout<<"\nThe average Turn Around time is : "<<avgTurnAroundTime;
    
    
    return 0;
}
