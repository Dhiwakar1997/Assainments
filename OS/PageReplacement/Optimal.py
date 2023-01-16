pageSeq= [4,6,2,5,1,8,3,1,0]#[1,2,3,4,1,2,5,1,2,3,4,5]

print(f"Page access sequence: {pageSeq}\n")

removeIndex = -1
memoryStrack = []

memSize = 3

for index, pageNo in enumerate(pageSeq):
    rank = []
    #print(f"Mem Seq: {memoryStrack}")
    
    if index<memSize:
        memoryStrack.append(pageNo)
    
    else:
        reverceList = pageSeq[index:].copy()
        #print(reverceList)
            
        for pageNoBack in  reverceList:
            if pageNoBack in memoryStrack and pageNoBack not in rank:
                rank.append(pageNoBack)
        #print(f"rank: {rank}")
        
        if pageNo not in memoryStrack:
            if rank:
                lruVal = rank.pop()
            else:
                removeIndex = (removeIndex+1)%memSize;
                lruVal = memoryStrack[removeIndex]
                
            for index_m, memLoc in enumerate(memoryStrack):
                if memLoc == lruVal:
                    memoryStrack[index_m] = pageNo
    
    print(memoryStrack)
