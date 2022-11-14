arr = [ 2,13,5,7,9,3 ]
requiredSubset = 25
wi=0
wk = sum(arr)



def condition1(wi_index:int, wk_next_index:int, requiredSubset:int) -> bool:
    wi_summation = sum(arr[:wi_index+1])
    wk_next = arr[wk_next_index]
    return wi_summation + wk_next  <= requiredSubset

def condition2(wi_index:int, wk_index:int, requiredSubset:int) -> bool:
    wi_summation = sum(arr[:wi_index+1])
    wk_next_summation = sum(arr[wk_index:])
    return wi_summation + wk_next_summation > requiredSubset


result = [0]*len(arr)

def sumOfSubset(wi:int, wk:int, index:int, index_included:bool):
    val = arr[index]
    wk -= val
    if wk==requiredSubset:
        return result
    elif condition1() and condition2():
        return sumOfSubset()
    else:
        return sumOfSubset()

    
