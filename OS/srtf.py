processList = ['PI', 'P2', 'P3', 'P4']
burstTime=[8,4,9,5]

arrivalTime = [2,1,0,3]
runningTime=0
liveBurstTime={}
waitingTimeResult = {}
turnAroundTimeDict ={}
completedList =[]
waitingTime=0


while (True):

    completedProcess = ""
    for i,at in enumerate(arrivalTime):
        if at<=runningTime and processList[i] not in liveBurstTime.keys () \
        and processList[i] not in completedList: liveBurstTime[processList[i]]=burstTime[i]
        waitingTimeResult[processList[i]]= 0
        turnAroundTimeDict [processList[i]] = 0
    min = float (' inf')
    minKey=''
    for key,val in liveBurstTime.items () :
        if val<=0:
            completedProcess = key
        if val<min and val>0:
            min=val 
            minKey=key 
    if completedProcess:
        completedList.append (completedProcess)
        completedList.append (completedProcess)
        del liveBurstTime [completedProcess]
    if minKey:
        liveBurstTime[minKey] = min-1
    for i in liveBurstTime:
        if i != minKey:
            waitingTimeResult[i]+=1
        turnAroundTimeDict[i]+=1
        runningTime+=1 
    if liveBurstTime=={}:
        break 

print(waitingTimeResult)
waitingTime=0
turnAroundTime=0
for i in processList:
    waitingTime+=waitingTimeResult[i] 
    turnAroundTime+=turnAroundTimeDict[i]
print (turnAroundTimeDict)
print(f'Total Waiting Time : (waitingTime]')
print (f'Average Waiting Time : {waitingTime/len (processList)}')
print (f'Total Turn Around Time : {turnAroundTime}')
print (f'Average Turn Around Time : {turnAroundTime/len(processList)}')
