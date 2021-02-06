def find_subset(array, n, table, sum) : 

    if (sum == 0 and len(table)!=0): 
        for value in table : 
            print(value, end=" ") 
        print("") 
        return
      
    if (n == 0): 
        return
  
    find_subset(array, n - 1, table, sum) 
    temp = [] + table 
    temp.append(array[n - 1]) 
    find_subset(array, n - 1, temp, sum - array[n - 1]) 


array = [2, 3, -5, -8, 6, -1]
print("Numbers:", array)
find_subset(array, len(array),[], 0) 