"""
    23-for O(log) we can code binary_search example that every time that run that code complixity decrease

    ----
    this example is about finding maximum number.for this must check all the elements in array.
    so if array has many number,complexity increase too

"""


nums=[2,16,7,9,8,23,12]

def show(list):
    max_num=list[0]
    for number in list:
        if number >max_num:
            max_num=number
    
    return max_num

print(show(nums))