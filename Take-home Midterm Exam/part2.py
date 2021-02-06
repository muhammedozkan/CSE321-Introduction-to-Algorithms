def FindMissingNumber(arr):
    
    result = 0
    for k in arr:
        result = result ^ k
 
    for k in range(0, len(arr) + 1):
        result = result ^ k

    return result
 
if __name__ == '__main__':
 
    arr = [0b000, 0b0001, 0b0011, 0b0010]
    print("Missing number is", FindMissingNumber(arr))