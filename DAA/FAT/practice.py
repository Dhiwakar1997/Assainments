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
# inputArr = [3,10,15,20]
# result = [0]*len(inputArr)
# reqSum=33
# def sumOfsubset(wi,index,wk):
#     result[index]=1
#     if wi+inputArr[index] == reqSum:
#         return result
#     elif wi+inputArr[index]+ inputArr[index+1] <=reqSum:
#         return sumOfsubset(wi+inputArr[index], index+1, wk-inputArr[index])
#     elif wi+wk-inputArr[index]>=reqSum and wi+inputArr[index]<=reqSum:
#         result[index]=0
#         return sumOfsubset(wi,index+1,wk-inputArr[index])
# sumOfsubset(0,0,sum(inputArr))
# print(result)

# d = 256

# # pat -> pattern
# # txt -> text
# # q -> A prime number


# def search(pat, txt, q):
#         p_len = len(pat)
#         t_len = len(txt)
#         i = 0
#         match_index = 0
#         p_hash = 0 # hash value for pattern
#         t_hash = 0 # hash value for txt
#         h = 1

#         for i in range(p_len-1):
#             h = (h*d)%q

#         for i in range(p_len):
#             p_hash =( d*p_hash + ord(pat[i]))%q
#             t_hash =( d*t_hash + ord(txt[i]))%q

#         for i in range(t_len-p_len +1):
#             print(p_hash,t_hash)
#             if p_hash == t_hash:
#                 for j in range(p_len):
#                     if txt[i+j] != pat[j]:
#                         break
#                     else:
#                         match_index += 1

#                 # if p_hash == t_hash and pat[0...p_len-1] = txt[i, i+1, ...i+p_len-1]
#                 if match_index == p_len:
#                     print(f"Pattern '{txt[i:i+p_len]}' found at index " + str(i))
#                     return

#             if i < t_len-p_len:
#                 t_hash = (d*(t_hash-ord(txt[i])*h) + ord(txt[i+p_len])) % q
            
#                 if t_hash <0:
#                     t_hash = t_hash +q

# txt = "CATS AND DOGS"
# pat = "DOG"
# q = 101
# print(search(pat,txt,q))

def knapSack(W,wt,val,n):
    if n==0 or W == 0:
        return 0
    
    if wt[n-1]>W:
        return knapSack(W,wt,val,n-1)

    else:
        return max(val[n-1]+knapSack(W-wt[n-1],wt,val,n-1),knapSack(W,wt,val,n-1))

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
