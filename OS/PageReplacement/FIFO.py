pageSeq= [4,6,2,5,1,8,3,1,0]#[1,2,3,4,1,2,5,1,2,3,4,5]

print(f"Page access sequence: {pageSeq}\n")

removeIndex = -1
memoryStrack = []

memSize = 3

for index, pageNo in enumerate(pageSeq):
    rank = []

    
    if index<memSize:
        memoryStrack.append(pageNo)
    
    else:
        
        if pageNo in memoryStrack:
            continue
        
        for i in pageSeq:
            if i in memoryStrack:
                lruVal = i
                break
        
        for index_m, memLoc in enumerate(memoryStrack):
            if memLoc == lruVal:
                memoryStrack[index_m] = pageNo

    
    print(f"Mem Seq: {memoryStrack}")
            
