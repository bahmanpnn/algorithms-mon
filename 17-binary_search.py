"""
    binary search has diffrent way to search the number that we give as input of function
    it checking the mid value of list; if the number is bigger than the number we give it check left side of the mid
    otherwise it check right side values of the mid number and return index of the target number
    [2,3,4,6,11,18,20,21] ,11 ==>4

"""

def binary_search(sequence,element):
    low,high=0,len(sequence)-1

    while low <=high:
        mid=(high+low) //2
        val=sequence[mid]
        if val == element:
            return mid
        elif val <element:
            low=mid+1
        else:
            high=mid-1
    
    return -1

print(binary_search([2,3,4,6,11,18,20,21],11))
