"""
    we need extra things over code working.it's about time and space complexity
    sometime we need more space so we must foc on space complexity or sometimes time is important!
    so in addittion to code working we must care about time and space in projects
    first complexity is o(1) that is fastest complexity and is constant time and it does not matter that 
    how many numbers is in list.because check just first number(array[0]) in list.
    
    ***in addittion to complexity has a data structure part that effect on complexity like where
    we use array,list,tuple,...

    nums=[1,12,3,4,2,1,13]
    nums=[1,12,3,4,2,1,13,4,54242,341]
"""

def show(list):
    if list[0] %2==0:
        return True
    else:
        return False
    
print(show([1,12,3,4,2,1,13]))