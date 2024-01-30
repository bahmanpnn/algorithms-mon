"""
polynomial time with bubble sort algorithm
its about o(n^n) and every code that check sequences more than one time
it makes more complexity and it takes more time to run
this example(bubble sort check sequence items 2 times)
so it's o(n^2) :))


nums=[64,35,25,32,11,90]
"""

def bubble_sort(collection):
    length=len(collection)
    for i in range(length-1):
        swapped=False
        for j in range(length-1-i):
            if collection[j] >collection[j+1]:
                swapped=True
                collection[j],collection[j+1]=collection[j+1],collection[j]
        
        if not swapped:
            break
    return collection


collection=[64,35,25,32,11,90]

print(bubble_sort(collection))