# lcs_result = ''

# def LCS(i,j,out):
#     if i==str1_len or j==str1_len:
#         return 0,out
#     elif string1[i]==string2[j]:
#         out+=string1[i]
#         temp, out = LCS(i+1,j+1,out)
#         return 1+temp, out
#     else:
#         lcs_result = out
#         return maxOfLCS(LCS(i+1,j,out),LCS(i,j+1,out))

# def maxOfLCS(A,B):
#     a,a_out = A
#     b,b_out = B
#     if a>b:
#         return a, a_out
#     else:
#         return b, b_out

# if __name__ == "__main__":
#     string1 = input("Enter the string 1: ") #aggtab
#     string2 = input("Enter the string 2: ") #gxtxayb
#     str1_len= len(string1)
#     str2_len= len(string2)

#     LCS_count, LCS_string = LCS(0,0,'')

#     print(f"The longest subsequence of string '{string1}' and string 2 '{string2}' is '{LCS_string}'")
#     print(f'The LCS count is {LCS_count}')


