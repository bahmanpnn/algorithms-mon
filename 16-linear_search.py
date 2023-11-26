"""
    this algorithm is searching a number in a list with simple loop and steps
    [1,2,5,8,11,14,18,23,32,48],11 ==> 4

"""

def linear_search(list,number):
    for i in range(len(list)):
        if list[i]==number:
            return i
        
    return -1

print(linear_search([1,2,5,8,11,14,18,23,32,48],11))
# print(linear_search([1,2,5,8,11,14,18,23,32,48],111))