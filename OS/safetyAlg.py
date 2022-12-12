numOfResource = 3
available = [3,3,2]#[0,0,0]#
allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]] #[[0,1,0],[2,0,0],[3,0,3],[2,1,1],[0,0,2]]#
maxDemand = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]] #[[0,0,0],[2,0,2],[0,0,0],[1,0,0],[0,0,2]]#
safeSeq = []
safeState = False

def mat2dDisplay(mat):
    for i in mat:
        for j in i:
            print(j,end="\t")
        print('\n')


need = []
for i in range(len(maxDemand)):
    temp=[]
    for j in range(numOfResource):
       temp.append(maxDemand[i][j]- allocation[i][j])
    need.append(temp)

def displaySeq():
    if safeState:

        print('\nSafe Sequence: \n')
        for i, val in enumerate(safeSeq):
            print(f" {val} ",end="")
            if i != len(safeSeq)-1:
                print(" -> ",end="")
        print('\n')
    else:
        print('\nSystem is Unsafe, Thus no safe sequence\n')


def safetyAlg(available, need):

    def step_2():
        doable_flag = False
        for process_index, fin in enumerate(finish):
            if not fin:
                doable_flag = True
                for need_index ,need_i in enumerate(need[process_index]):
                    if need_i > work[need_index]:
                        doable_flag = False  
                if doable_flag:
                    #print(f"P{process_index}")
                    safeSeq.append(f"P{process_index}")
                    step_3(allocation[process_index], process_index)
        if not doable_flag:
            step_4()


    def step_3(allocation, process_index):
        #print(allocation)
        finish[process_index] = True 
        for index, allocation_val in enumerate(allocation):
            work[index] = work[index] + allocation_val
        #print(work)
        step_2()


    def step_4():
        global safeState
        complete = True
        #print(finish)
        for process_index, fin in enumerate(finish):
             if not fin:
                complete = False
        if complete:
            #print("\nSystem is safe\n")
            safeState = True
        else:
            #print("\nSystem is unsafe")
            safeState = False

    #step 1
    work = available
    finish = [False for i in need]

    #step 2 : Find an i such that - finish[i] = false && need[i]<=work
    step_2()

    #step 3 : work = work + allocation[i] -> finish[i]=True -> goto step 2

    #step 4 : if finish[i]=True for all i, then the system is in safe state

    return  safeState

def resourceReq(available, process_index, req):
    global safeSeq

    def revert(process_index, req):
        for index, val in enumerate(allocation[process_index]):
            allocation[process_index][index] = allocation[process_index][index]  + req[index]
            need[process_index][index] = need[process_index][index]  - req[index]

    for index, val in enumerate(allocation[process_index]):
        allocation[process_index][index] = allocation[process_index][index] - req[index]
        need[process_index][index] = need[process_index][index]  + req[index]
    
    temp = safeSeq.copy()
    safeSeq = []
    doable = safetyAlg(available, need)
    if doable:
        print(f"Request {req} to process P{process_index} is doable, System is safe")
    else:
        revert(process_index, req)
        safeSeq = temp
        print(f"Request {req} to process P{process_index} results in Unsafe state")


print("Allocation:")
mat2dDisplay(allocation)

print("Max Demand:")
mat2dDisplay(maxDemand)

print("Need:")
mat2dDisplay(need)

print("Available:")
for i in available:
    print(i,end='\t')
print("\n")

safetyAlg(available.copy(), need)

displaySeq()
resourceReq(available.copy(), 1, (1,0,2))

displaySeq()
resourceReq(available.copy(), 2, (200,300,230))
displaySeq()



