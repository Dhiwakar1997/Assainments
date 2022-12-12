numOfResource = 3
available = [3,3,2]#[0,0,0]#
allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]] #[[0,1,0],[2,0,0],[3,0,3],[2,1,1],[0,0,2]]#
maxDemand = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]] #[[0,0,0],[2,0,2],[0,0,0],[1,0,0],[0,0,2]]#
need = []
for i in range(len(maxDemand)):
    temp=[]
    for j in range(numOfResource):
       temp.append(maxDemand[i][j]- allocation[i][j])
    need.append(temp)

print("Allocation:")
for i in range(len(allocation)):
    for j in range(numOfResource):
        print(f"{allocation[i][j]}\t",end='')
    print("\n")

print("Need:")
for i in range(len(need)):
    for j in range(numOfResource):
        print(f"{need[i][j]}\t",end='')
    print("\n")

print("Available:")

for j in range(numOfResource):
    print(f"{available[j]}\t",end='')
print("\n")

delayedAllocation = []
delayedNeed = []
processCount = len(need)
processSequence = [i for i in range(len(need))]
completedSeq = []
delayedSeq = []

travelingIndex = 0
while len(completedSeq)< processCount :
    if travelingIndex<len(processSequence):
        currentProcess = processSequence[travelingIndex]
        currentAllocation = allocation[travelingIndex]
        currentNeed = need[travelingIndex]
        feasible_flag = True
        for index in range(numOfResource):
            if currentNeed[index] > available[index]:
                feasible_flag=False
        if feasible_flag:
            for index in range(numOfResource):
                available[index] += currentAllocation[index]
            completedSeq.append(currentProcess)
        else:
            delayedSeq.append(currentProcess)
        travelingIndex+=1
    else:
        for index in delayedSeq:
            currentProcess = processSequence[index]
            currentAllocation = allocation[index]
            currentNeed = need[index]
            for index in range(numOfResource):
                available[index] += currentAllocation[index]
            completedSeq.append(currentProcess)
#print(completedSeq)

print("\nProcess completion is: \n")
for i in completedSeq:
    print(f" P{i} -> ",end="")

print('\n')
    
    