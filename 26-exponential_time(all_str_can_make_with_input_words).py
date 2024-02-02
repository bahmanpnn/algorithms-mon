"""
    this algorithm tries to show complexity of items in list that uses n time
    to know how many times we can make diffrent words with items of list 
    
    ==>O(2^n) is main but input list has  4 item so it is O(4^n) ===>O(n^n)

    ['a','b','c','d']==> abcd,bcad,cbad,.... ===> 4**2=16    
    
    ***remember that O(2^n) has more complexity than O(n^2)
""" 

from itertools import chain,combinations

def subsets(iterable):
    s=list(iterable)
    return list(chain.from_iterable(combinations(s,r) for r in range(len(s)+1)))


my_list=['a','b','c','d']

print(subsets(my_list))