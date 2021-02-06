def xth_element(A, B, m, n, xth,flag):
    if flag==1:
        A.sort()
        B.sort()
    if m > n:  # switch arrays to make m <= n
        return xth_element(B, A, n, m, xth,0)
    if m == 0:
        return B[xth - 1]
    if xth == 1:
        return min(A[0], B[0])

    i = min(m, xth // 2)
    j = min(n, xth // 2)
    if A[i - 1] > B[j - 1]:
        return xth_element(A, B[j:], m, n - j, xth - j,0)
    else:
        return xth_element(A[i:], B, m - i, n, xth - i,0)
        
def driver_xth_element():
    A = [25, 9, 14, 19, 16,4]
    B = [15, 32, 11, 2, 23, 5]
    print(A + B)
    
    result = xth_element(A, B, len(A),len(B), 7,1)
    print(result)
    
driver_xth_element()