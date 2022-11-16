lcs_result = ''

def maximum_LCS(a_tuple,b_tuple):
    a,a_out = a_tuple
    b,b_out = b_tuple
    if a>b:
        return a, a_out
    else: 
        return b, b_out

def LCS(i,j,out):
    global lcs_result
    if i== str1_length or j==str2_length:
        return 0 , out
    elif string1[i]==string2[j]:
        out += string1[i]
        temp, out = LCS(i+1,j+1, out)
        return (1 + temp) , out
    else: 
        lcs_result = out
        return maximum_LCS(LCS(i+1,j,out), LCS(i,j+1,out))

if __name__ == "__main__":
    string1 = input("Enter the string 1: ") #aggtab
    string2 = input("Enter the string 2: ") #gxtxayb
    str1_length = len(string1)
    str2_length = len(string2)

    LCS_count, LCS_string = LCS(0,0,'')

    print(f"The longest subsequence of string '{string1}' and string 2 '{string2}' is '{LCS_string}'")
    print(f'The LCS count is {LCS_count}')
