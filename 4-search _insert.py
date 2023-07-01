
"""
[1,3,5,6],3 ==>1
[1,3,5,6],4 ==>2
[1,3,5,6],7 ==>4
[1,3,5,6],0 ==>0
"""

def search_insert(array,val):
    low=0
    high=len(array)-1
    mid=high //2

    while low <=high:
        if val >array[mid]:
            mid+=1
            low=mid
        else:
            mid-=1
            high=mid
    
    return low


print(search_insert([1,3,5,6],7))