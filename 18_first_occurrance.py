"""
    this algorithm tries to find the index of first element that quals in list,
    find the first occurrence of a number using the binary search algorithm  
    Defining a function to find the first occurrence, which will take the array of integers,
    and the number we have to search for    
    
    **this algorithm uses binary algorithm
    [2,2,2,3,3,4,4,5,5,5],4 ==> 5

        while low<= high:  
        # Finding the middle index of the list based on the current s and e positions  
        mid = (low + high) // 2   

        # Checking if the middle element is equal to x  
        # If yes, we will store the middle index in the result and then search in the left half  
        if array[mid] == element:  
            result = mid  
            high = mid - 1  
        
        # If the middle element is greater than x then search in the left half  
        elif array[mid] > element:  
            high = mid - 1   
        
        # Else search in the right half  
        else:  
            low = mid + 1
"""

def first_occurance(array,element):
    
    low,high=0,len(array)
    while low<=high:
        mid=(low+high) //2

        #if the element doesnt exist in array this condition causes breaking from loop
        if low ==high:
            break

        if array[mid]<element:
            low=mid+1
        
        else:
            high=mid

    if array[low] ==element:
        return low



print(first_occurance([2,2,2,3,3,4,4,5,5,5],7))