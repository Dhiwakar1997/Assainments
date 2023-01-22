timeQuantum = 3
burstTime = {"p0":24,"p1":3,'p2':3}
waitingTime = {f'p{i}':0 for i in range(len(burstTime))}
turnAroundTime = {f'p{i}':1 for i in range(len(burstTime))}
completed = []
burstTimeCopy = burstTime.copy()
totalWaitingTime = 0
totalTurnAroundTime = 0
index = -1
loopCycle = 0

while len(burstTimeCopy)!=0:

    if loopCycle%(timeQuantum)==0 :
        loopCycle=1
        index=index+1
    else:
        loopCycle+=1

    if index==len(burstTime):
        index=0
    #print(f"\nIndex = {index}")
    #print(f"LoopCycle = {loopCycle}")
    if f'p{index}' in completed:
        continue

    burstTimeCopy[f'p{index}']-=1

    if burstTimeCopy[f'p{index}'] == 0:
        completed.append(f'p{index}')
        del burstTimeCopy[f'p{index}']
        

    for pros in waitingTime.keys():
        if pros not in completed:
            if pros != f'p{index}':
                waitingTime[pros] +=1
            turnAroundTime[pros] +=1
    
for key,wt in waitingTime.items():    
    totalWaitingTime+=wt
    totalTurnAroundTime+=turnAroundTime[key]

avgWaitingTime = totalWaitingTime/len(burstTime)
avgTurnAroundTime = totalTurnAroundTime/len(burstTime)

for process, wt in waitingTime.items():
    print(f'The process {process} waiting time is "{wt}" ')
    
print('\n')
print(f'Total waiting time: {totalWaitingTime}')
print(f'Average waiting time: {round(avgWaitingTime, 2)}')
print('\n')

for process, tat in turnAroundTime.items():
    print(f'The process {process} waiting time is "{tat}" ')
print('\n')
print(f'Total turnaround time: {totalTurnAroundTime}')
print(f'Average turnaround time: {round(avgTurnAroundTime, 2)}')
