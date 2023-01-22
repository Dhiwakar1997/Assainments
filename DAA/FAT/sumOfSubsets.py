inputArray = [ 2,13,5,7,9,3 ]
requiredSubset = 22
wi=0
wk = sum(inputArray)

result = [0]*len(inputArray)

def sumOfSubset(wi:int, index:int, wk:int):

    result[index] = 1
    if wi+inputArray[index]==requiredSubset:
        return result
    elif wi+inputArray[index]+inputArray[index+1]<=requiredSubset:
        return sumOfSubset(wi+inputArray[index],index+1, wk-inputArray[index])
    elif wi+wk-inputArray[index]>=requiredSubset and wi+inputArray[index+1]<=requiredSubset:
        result[index]=0
        return sumOfSubset(wi,index+1,wk-inputArray[index])

sumOfSubset(wi,0,wk)

print(f"The given array of elements : {inputArray}")
print(f"Required Subset : {requiredSubset}")
print(f"The result of the subset : {result}")
