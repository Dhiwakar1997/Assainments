queue = [98, 183, 37, 122, 14, 124,65,67]
currentPosition = 53
minDist = float("inf")
nearestPosition = currentPosition
totalMovement = 0
flowPath = []

for i in range(len(queue)):
    for element in queue:
        if abs(currentPosition - element) <= minDist:
            minDist = abs(currentPosition - element)
            nearestPosition = element
    flowPath.append(nearestPosition)
    queue.remove(nearestPosition)
    currentPosition = nearestPosition   
    totalMovement += minDist    
    minDist = float("inf")

print(f"Total Movement: {totalMovement}")
print("The Shortest Seek Time First(SSTF) path is: ")
for i in flowPath:
    print(f"{i} -> ",end="")
print('\n')
