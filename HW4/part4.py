def different(A, B,samplescale):
    if type(A) == list:
        if sum(A) == (len(A)*samplescale):
            return B
        else:
            return A
    else:
        if A == samplescale:
            return B
        else:
            return A


def find_incorrectly_bottle(lst,samplescale):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return different(lst[0], lst[1],samplescale)
    
    A = lst[0: len(lst) // 2]
    B = lst[len(lst) // 2:len(lst)]

    return find_incorrectly_bottle(different(A, B,samplescale),samplescale)
    
def driver_find_incorrectly_bottle():
    bottles = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,5,5,5,5,5,5,5]  
    samplescale=5
    
    print("bottles: ", bottles)
    print("bottle is incorrectly: ", find_incorrectly_bottle(bottles,samplescale))
    
driver_find_incorrectly_bottle() 