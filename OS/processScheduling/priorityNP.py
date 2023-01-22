
#Non Preemptive

burstTime = {'p1':6,'p2':8,'p3':2}
priority = {'p1':3,'p2':2,'p3':1}
totalWaitingTime = 0
totalTurnAroundTime = 0
waitingTime = {}
turnAroundTime = {}
currentTime = 0

priorityOrder = list(priority.values())
priorityOrder.sort()

priorityList = []
for p in priorityOrder:
    for key,val in priority.items():
        if val == p:
            priorityList.append(key)

for ps in priorityList:
    waitingTime[ps] = currentTime
    currentTime += burstTime[ps]
    turnAroundTime[ps] = currentTime



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
