pageSeq= [4,6,2,5,1,8,3,1,0]#[1,2,3,4,1,2,5,1,2,3,4,5]

print(f"Page access sequence: {pageSeq}\n")

memoryStrack = []

memSize = 3

for index, pageNo in enumerate(pageSeq):
    rank = []
    
    if index<memSize:
        memoryStrack.append(pageNo)
    
    else:
        reverceList = pageSeq[index:0:-1].copy()
        reverceList.append(pageSeq[0])
        #print(reverceList)
            
        for pageNoBack in  reverceList:
            if pageNoBack in memoryStrack and pageNoBack not in rank:
                rank.append(pageNoBack)
        #print(rank)
        
        if pageNo not in memoryStrack:
            lruVal = rank.pop()
            
            for index_m, memLoc in enumerate(memoryStrack):
                if memLoc == lruVal:
                    memoryStrack[index_m] = pageNo
    
    print(memoryStrack)
