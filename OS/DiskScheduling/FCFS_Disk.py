queue = [98, 183, 37, 122, 14, 124,65,67]
currentPosition = 53
flowPath = [ currentPosition ]
totalMovement = 0
for element in queue:
    totalMovement += abs(currentPosition-element)
    flowPath.append(element)
    currentPosition = element

print(f"Total Movement: {totalMovement}")
print("The First Come First Serve(FCFS) path is: ")
for i in flowPath:
    print(f"{i} -> ",end="")
print('\n')
