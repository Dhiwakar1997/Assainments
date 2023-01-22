processList = ['P1', 'P2', 'P3', 'P4']
burstTime=[8,4,9,5]

arrivalTime = [2,1,0,3]
priority = [3,1,0,2]
currentPriority = []
runningTime=0
liveBurstTime={}
waitingTimeResult = {}
turnAroundTimeDict ={}
completedList =[]
totalWaitingTime=0

k=0
while(True):
    k+=1
    completedProcess = ""
    for i,at in enumerate(arrivalTime):
        if at<=runningTime and processList[i] not in liveBurstTime.keys () \
        and processList[i] not in completedList: 
            liveBurstTime[processList[i]]=burstTime[i]
            waitingTimeResult[processList[i]]= 0
            turnAroundTimeDict [processList[i]] = 0
    currentPriority=[]
    for key,val in liveBurstTime.items():
        currentPriority.append(priority[processList.index(key)])

    maxPriority = max(currentPriority)
    maxKey= processList[priority.index(maxPriority)] 

    if liveBurstTime[maxKey]<=0:
        completedProcess = maxKey
    
    if completedProcess:
        completedList.append (completedProcess)
        completedList.append (completedProcess)
        del liveBurstTime [completedProcess]
        toBeRemoved = max(currentPriority)
        currentPriority.pop(currentPriority.index(toBeRemoved))

    if maxKey in liveBurstTime:
        liveBurstTime[maxKey] = liveBurstTime[maxKey]-1
    for i in liveBurstTime:
        if i != maxKey:
            waitingTimeResult[i]+=1
        turnAroundTimeDict[i]+=1
        runningTime+=1 
    if liveBurstTime=={}:
        break 

totalWaitingTime=0
totalTurnAroundTime=0
for i in processList:
    totalWaitingTime+=waitingTimeResult[i] 
    totalTurnAroundTime+=turnAroundTimeDict[i]

avgWaitingTime = totalWaitingTime/len(burstTime)
avgTurnAroundTime = totalTurnAroundTime/len(burstTime)


for process, wt in waitingTimeResult.items():
    print(f'The process {process} waiting time is "{wt}" ')
    
print('\n')
print(f'Total waiting time: {totalWaitingTime}')
print(f'Average waiting time: {round(avgWaitingTime, 2)}')
print('\n')

for process, tat in turnAroundTimeDict.items():
    print(f'The process {process} waiting time is "{tat}" ')
print('\n')
print(f'Total turnaround time: {totalTurnAroundTime}')
print(f'Average turnaround time: {round(avgTurnAroundTime, 2)}')
