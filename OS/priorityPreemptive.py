
# Preemptive

burstTime = {"p1":24,"p2":3,'p3':3}
priority = {'p1':0,'p2':2,'p3':1}
arrivalTime = {'p1':0,'p2':2,'p3':3}
waitingTime = {f'p{i}':0 for i in range(len(burstTime))}
turnAroundTime = {f'p{i}':1 for i in range(len(burstTime))}
liveBurstTime = {}
currentTime = -1
i=1
while True:
    currentTime+=1
    for key, val in arrivalTime.items():
        if currentTime==val:
            liveBurstTime[key]= burstTime[key]
    print(liveBurstTime)

    priorityOrder = list(priority.values())
    priorityOrder.sort(reverse=True)

    priorityList = []
    for p in priorityOrder:
        for key,val in priority.items():
            if val == p and key in liveBurstTime:
                priorityList.append(key)
    print(priorityList)

    i+=1
    if i == 10:
        break