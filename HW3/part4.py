import random 

def insertion_sort(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        sorted_idx = i - 1
        while sorted_idx >= 0 and lst[sorted_idx] > item:
            lst[sorted_idx + 1] = lst[sorted_idx]  # swap operation performed
            sorted_idx -= 1
        lst[sorted_idx + 1] = item


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


def driver_insertion_sort():
    lst = [random.randint(i, i + 10) for i in range(10)]
    print("Unsorted list: ", lst)
    insertion_sort(lst)
    print("Sorted list (via Insertion Sort): ", lst)

def driver_quick_sort():
    lst = [random.randint(i, i + 10) for i in range(10)]
    print("Unsorted list: ", lst)
    quick_sort(lst, 0, len(lst) - 1)
    print("Sorted list (via Quick Sort): ", lst)

driver_insertion_sort()
print(" ") 
driver_quick_sort()