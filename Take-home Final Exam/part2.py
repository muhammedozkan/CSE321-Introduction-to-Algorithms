def quick_sort(lst, low_idx, high_idx):
    if low_idx < high_idx:
        partition_idx = partition(lst, low_idx, high_idx)
        quick_sort(lst, low_idx, partition_idx - 1)
        quick_sort(lst, partition_idx + 1, high_idx)


def partition(lst, low_idx, high_idx):
    smaller_idx = low_idx - 1
    pivot = lst[high_idx]
    for j in range(low_idx, high_idx):
        if lst[j] < pivot:
            smaller_idx = smaller_idx + 1
            swap(lst, smaller_idx, j)
    swap(lst, smaller_idx + 1, high_idx)
    return smaller_idx + 1
    
def swap(lst, idx1, idx2):
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp
    
def findMinIntervalMethod1(Array,i,j):
    temp=Array[i-1:j-1]
    quick_sort(temp,0,len(temp)-1)
    return temp[0]

def findMinIntervalMethod2(Array,i,j):
    quick_sort(Array,0,len(Array)-1)
    temp=Array[i-1:j-1]
    return temp[0]

lst = [7,3,9,10,5,4,1,15,17,32,5,7,0]
print("Method1")
print("Interval [1,9]",findMinIntervalMethod1(lst,1,9))
print(lst)
print(" ")
lst = [7,3,9,10,5,4,1,15,17,32,5,7,0]
print("Method2")
print("Interval [1,9]",findMinIntervalMethod2(lst,1,9))
print(lst)