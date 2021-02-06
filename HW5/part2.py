def minSumPath(triangle): 
      
    table = [0] * len(triangle) 
    n = len(triangle) - 1
      
    for i in range(len(triangle[n])):  
        table[i] = triangle[n][i]  
        
        
    for i in range(len(triangle) - 2, -1,-1):  
        for j in range( len(triangle[i])):  
            table[j] = triangle[i][j] + min(table[j],table[j + 1]); 
         
        
    return table[0] 
  

A = [[ 2 ], 
    [5, 4 ], 
   [1, 4, 7 ], 
  [8, 6, 9, 6]] 
print(minSumPath(A)) 