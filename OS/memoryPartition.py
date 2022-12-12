availableMemorySpace = [100,500,200,300,600]
requestSpace = [212,417,112,426]

def firstFit(availableMemorySpace,requestSpace):
    memorySeq = []
    print('\n')
    for req in requestSpace:
        done = 0
        for index, available in enumerate(availableMemorySpace):

            if(req<available):
                memorySeq.append(f"P{index}")
                availableMemorySpace[index] -=req
                done =1
                break
        if done == 0:
            print(f"Memory has no space to fit {req}")
            memorySeq.append(None)
    print("First Fit Sequence:")
    print(memorySeq)
    return memorySeq

firstFitMemorySeq = firstFit(availableMemorySpace.copy(),requestSpace) 

def bestFit(availableMemorySpace,requestSpace):
    memorySeq = []
    print('\n')
    for req in requestSpace:
        minVal = float('inf')
        minValIndex = 0
        for index, available in enumerate(availableMemorySpace):
            p = available - req
            if p<minVal and p>0:
                minVal = p
                minValIndex = index
        memorySeq.append(f"P{minValIndex}")
        availableMemorySpace[minValIndex] -= req 
        #print(availableMemorySpace)
    print("Best Fit Sequence:")
    print(memorySeq)

bestFitMemorySeq = bestFit(availableMemorySpace.copy(),requestSpace)


def worstFit(availableMemorySpace,requestSpace):
    memorySeq = []
    print('\n')
    for req in requestSpace:
        maxVal = float('-inf')
        maxValIndex = 0
        for index, available in enumerate(availableMemorySpace):
            p = available - req
            if p>maxVal and p>0:
                maxVal = p
                maxValIndex = index

        if maxVal >0:
            memorySeq.append(f"P{maxValIndex}")
            availableMemorySpace[maxValIndex] -= req 
        else:
            print(f"Memory has no space to fit {req}")
            memorySeq.append(None)
    print("Worst Fit Sequence:")
    print(memorySeq)

worstFitMemorySeq = worstFit(availableMemorySpace.copy(),requestSpace)