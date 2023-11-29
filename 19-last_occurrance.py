"""
    this algorithm is working opposite of first occurrance and tries to find last number in array that
    equals to element we give as input to function 

    [2,2,2,3,3,4,4,5,5,5],4 ==>6
"""

def last_occurrance(array,element):
    low,high=0,len(array)-1
    while low <=high:
        mid=(low+high) //2
        if (array[mid]==element and mid ==len(array)-1) or \
            (array[mid]==element and array[mid+1]) >element:
            return mid
        elif (array[mid]<=element):
            low=mid+1
        else:
            high=mid-1

print(last_occurrance([2,2,2,3,3,4,4,5,5,5],4))