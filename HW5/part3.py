def Knapsack(W, wt, val,n):
 
    table = [0 for i in range(W + 1)]
 
    ans = 0
 
    
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                table[i] = max(table[i], table[i - wt[j]] + val[j])
    print(table) 
    
    return table[W]
  

val = [10, 4, 3] 
wt = [5, 4, 2] 
W = 9
n = len(val) 

print(Knapsack(W, wt, val, n)) 
