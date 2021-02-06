def Insertion_Sort(arr, low, n): 
    for i in range(low + 1, n + 1): 
        val = arr[i] 
        j = i 
        while j>low and arr[j-1]>val: 
            arr[j]= arr[j-1] 
            j-= 1
        arr[j]= val 
  
def Partition(arr, low, high): 
    pivot = arr[high] 
    i = j = low 
    for i in range(low, high): 
        if arr[i]<pivot: 
            temp= array[i]
            array[i]= array[j]
            array[j]=temp
            j+= 1
    temp= array[j]
    array[j]= array[high]
    array[high]=temp
    return j 
  
def New_Quick_Sort(arr, low, high): 
    while low<high: 
        if high-low + 1<9: 
            Insertion_Sort(arr, low, high) 
            break
        else: 
            pivot = Partition(arr, low, high) 
            if pivot-low<high-pivot: 
                New_Quick_Sort(arr, low, pivot-1) 
                low = pivot + 1
            else: 
                New_Quick_Sort(arr, pivot + 1, high) 
                high = pivot-1
    return arr
    
if __name__ == '__main__':
  
    array = [ 13, 85, 51, 52, 98, 75, 23,56, 13, 35, 23, 91, 55, 12,39, 30, 72, 33, 7, 11, 94 ] 
    New_Quick_Sort(array, 0, len(array)-1) 
    print(array) 