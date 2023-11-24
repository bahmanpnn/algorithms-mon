"""
    this algorithm remove minimum number in sequence
    [4,5,2,8,-2,5,1,9] ==> -2

"""

def remove_min(sequence):
    storage_sequence=[]
    if len(sequence) == 0:
        return sequence
    
    min=sequence.pop()
    sequence.append(min)
    
    #check which number is minimum to save in min variable and append numbers in storage_sequence
    for i in range(len(sequence)):
        val=sequence.pop()
        if val <=min:
            min=val
        storage_sequence.append(val)
    
    # checking the storage_sequence numbers to append numbers again to sequence without minimum number
    for j in range(len(storage_sequence)):
        val=storage_sequence.pop()
        if val != min:
            sequence.append(val)
    
    return sequence,min

print(remove_min([4,5,2,8,-2,5,1,9]))