# a dynamic approach
# Returns the maximum value that can be stored by the bag
def knapSack(W, wt, p, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
   #Table in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                # print(p[i],wt[i])
                K[i][w] = max(p[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
#     print()
    return K[n][W]
#Main
prof = [1,2,5,6]
wt = [2,3,4,5]
W = 8
n = len(prof)
print(knapSack(W, wt, prof, n))
