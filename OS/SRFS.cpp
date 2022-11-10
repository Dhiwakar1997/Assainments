 #include<iostream>
using namespace std;

int main(){
    
    int processCount, currentTime=0;
    float avgWaitingTime,avgTurnAroundTime,waitingTime=0,turnAroundTime=0;
    cout<< "Enter the number of Processes: ";
    //cin>> processCount;
    processCount=4;
    int burstTime[processCount]={8,4,9,5}, 
    arraivalTime[processCount]={2,1,0,3},
    completionTime[processCount], 
    processOrder[processCount]={0,1,2,3};
    
    
    /*for(int i=0;i<processCount;i++){
        cout<<"\nEnter burst time of process "<<i+1<<" -";
        cin>>burstTime[i];
        cout<<"\nEnter arraival time of process "<<i+1<<" -";
        cin>>arraivalTime[i];
        processOrder[i]=i;
    }*/
    
    int runningTime=0;
    /*for(int i=0;i<processCount;i++){
        
    for(int j=i+1;j<processCount;j++){
        if(arraivalTime[i]>arraivalTime[j]){
            int temp;
            temp = processOrder[j];
            processOrder[j] = processOrder[i];
            processOrder[i] =temp;
            temp = burstTime[j];
            burstTime[j] = burstTime[i];
            burstTime[i]=temp;
        }
    } }
    for(int i=0;i<processCount;i++){
        cout<<"\nBT- "<<burstTime[i]<<" processOrder-"<<processOrder[i];
        
    }*/
    int liveBurstTime[processCount],liveListCount=0;
    
    while(runningTime<10){
        for(int i=0;i<processCount;i++){
            if(arraivalTime[i]<=runningTime){
            liveBurstTime[liveListCount]=burstTime[i];
            liveListCount++;
            }
        }
  
    int min = liveBurstTime[0],minPosision=0;    
        

    for (int i = 0; i < liveListCount; i++) {  
        cout<<"\nIndex: "<<i<<"liveBurstTime: "<<liveBurstTime[i];
 
       if(liveBurstTime[i] < min)    
       {
           min = liveBurstTime[i]; 
           minPosision = i;
    } 
    
    }
    cout<<"\nmin="<<min<<" minPosision="<<minPosision;
    liveListCount=0;
        runningTime++;
    }
    return 0;
}
