def pairedElements(arr, multiplication):
   
    low = 0;
    high = len(arr) - 1;
 
    while (low < high):
        if (arr[low] *  arr[high] == multiplication):
            print("(", arr[low],  ", ", arr[high], ")");
        if (arr[low] * arr[high] > multiplication):
            high -= 1;
        else:
            low += 1;
            
            
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
        
 
# Driver code
if __name__ == '__main__':
   
    arr = [1,2,3,6,5,4];
    mergeSort(arr);
    pairedElements(arr, 6);
