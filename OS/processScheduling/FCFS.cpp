#include<iostream>

using namespace std;

int main()
{
    int processCount, currentTime=0, sort_start, sort_destination;
    float avgWaitingTime,avgTurnAroundTime,waitingTime=0,turnAroundTime=0;
    cout<< "Enter the number of Processes: ";
    cin>> processCount;
    int burstTime[processCount], arrivalTime[processCount]
    ,completionTime[processCount], processOrder[processCount];
    
    
    for(int i=0;i<processCount;i++){
        cout<< "Enter process "<<i<<" burst time: ";
        cin>>burstTime[i];
        arrivalTime[i]=0;
    }
        
    for(int i=0;i<processCount;i++)
    {
        currentTime += burstTime[i];
        completionTime[i]=currentTime;
        turnAroundTime+=completionTime[i]-arrivalTime[i];
        if(i==0)continue;
        waitingTime+=completionTime[i-1]-arrivalTime[i-1];
    }    

    
    avgWaitingTime=waitingTime/processCount;
    avgTurnAroundTime=turnAroundTime/processCount;
    cout<<"\nThe Total Waiting time is : "<<waitingTime;
    cout<<"\nThe average Waiting time is : "<<avgWaitingTime;
    cout<<"\nThe Total Turn Around time is : "<<turnAroundTime;
    cout<<"\nThe average Turn Around time is : "<<avgTurnAroundTime<<'\n';
    
    
    return 0;
}
