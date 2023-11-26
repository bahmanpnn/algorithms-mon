"""
    this algorithm checking the sorted sequence and find the range of number that as parametr we give
    *** it just works on list with 7 numbers.just we can change numbers of list !!  
    [5,7,7,8,8,8,10],7 ==>[1,2]
    [5,7,7,8,8,8,10],8 ==>[3,5]

"""

def search_engine(sequence,target):
    
    low=0
    high=len(sequence)-1 
    
    while low<= high:
        # mid=high //2 
        mid=low+(high-low) //2
        
        if target<sequence[mid]:
            high =mid-1 

        elif target>sequence[mid]:
            low=mid+1
        
        else:
            break

    for j in range(len(sequence)-1,-1,-1):
        if sequence[j] ==target:
            return [mid,j]
        
    return [None,None]


print(search_engine([5,7,7,8,8,8,10],8))