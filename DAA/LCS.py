lcs_result = ''

def maximum(a,b):
    if a>b:
        return a
    else: 
        return b

def LCS(i,j):
    #print(f"i:{i},j:{j}")
    global lcs_result
    if i== str1_length or j==str2_length:
        return 0
    elif string1[i]==string2[j]:
        #lcs_result+= string1[i]
        return 1 + LCS(i+1,j+1)
    else: 
        return maximum(LCS(i+1,j), LCS(i,j+1))

if __name__ == "__main__":
    string1 = "aabcd" #input("Enter the string 1: ")
    string2 = "abcd" #input("Enter the string 2: ")
    str1_length = len(string1)
    str2_length = len(string2)


    LCS_count = LCS(0,0)
    #print(f"The longest subsequence of string '{string1}' and string 2 '{string2}' is '{lcs_result}'")
    print(f'The LCS count is {LCS_count}')
