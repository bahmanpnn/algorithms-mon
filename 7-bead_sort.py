"""
    this algorithm is about sorting without sort method to learn how it works!
    this algorithm maybe is not exactly the sort method but it is a way to sorting numbers in list 
    with bead checking and compare 2 by 2 numbers in list

    [4,7,2,9,3,6,7] ==>[2,3,4,6,7,7,9]
    0(4,7),1(7,2),2(2,9),...

    ----------

    1-any() is a method that returns true if any condition in it is true
    
    2-is_instance() is a method that return true if at least one condition in that be true
    isinstance(object, type)
    x = isinstance("Hello", (float, int, str, list, dict, tuple)) ==>true
    
    ----
    class myObj:
    name = "bahman"

    y = myObj()
    x = isinstance(y, myObj)

    print(x) ==>true
    ----
    
    3- enumerate() function takes a sequence and returns it as an enumerate object.
    adds a counter as the key of the enumerate object.
    enumerate(iterable, start)

    x = ('apple', 'banana', 'cherry')
    y = enumerate(x)
    print(list(y)) ==>  [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
    ----

    index = 0

    for value in values:
        print(index, value)
        index += 1
    0 a
    1 b
    2 c
    ---
    for index in range(len(values)):
        value = values[index]
        print(index, value)
    
    0 a
    1 b
    2 c
    ---
    for count, value in enumerate(values):
    print(count, value)
    
    0 a
    1 b
    2 c
    ---

    for count, value in enumerate(values, start=1):
    print(count, value)
    1 a
    2 b
    3 c
    ----

    4-zip The zip() function returns a zip object, which is an iterator of tuples where
    the first item in each passed iterator is paired together, and then the second item in
    each passed iterator are paired together etc.
    **remember that zip method return an object so we must use set or tuple or list and ... methods to show them

    a = ("John", "Charles", "Mike")
    b = ("Jenny", "Christy", "Monica", "Vicky")

    x = zip(a, b) 
    print(tuple(x)) / print(set(x)) / ... ==>(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
    
    ----- zip+enumerate
    names = ['Mukesh', 'Roni', 'Chari']
    ages = [24, 50, 18]

    for i, (name, age) in enumerate(zip(names, ages)):
	    print(i, name, age)===> 0 Mukesh 24
                            1 Roni 50
                            2 Chari 18

    ----
    stocks = ['GEEKS', 'For', 'geeks']
    prices = [2175, 1127, 2750]

    new_dict = {stocks: prices for stocks,
                prices in zip(stocks, prices)}
    print(new_dict)

"""

def bead_sort(sequence):

    if any(not isinstance(x,int) or x<0 for x in sequence):
        raise TypeError('sequence must be list on non-negative integers')
    
    # seq=[]
    for _ in range(len(sequence)):
        for count,(rod_upper,rod_lower) in enumerate(zip(sequence,sequence[1:])):
            # seq.append((count,rod_upper,rod_lower))
        # for count,(rod_upper,rod_lower) in enumerate(zip([4,7,2,9,3,6,7],[7,2,9,3,6,7])):
            # 0,4,7 ==>0,4,7 ==>0,4,2==>0,2,4
            # 1,7,2 ==>1,2,7 it swap in next lines and in enumerate 2 it checks 7,9 not 2,9
            # 2,2,9 ==>2,7,9
            # 3,9,3 ==>3,3,9
            # 4,3,6 ==>4,9,6 
            # 5,6,7 ==>5,9,7 

            if rod_upper>rod_lower:
                sequence[count] -= rod_upper-rod_lower
                sequence[count+1] += rod_upper-rod_lower

    return sequence
    # return seq

print(bead_sort([4,7,2,9,3,6,7]))