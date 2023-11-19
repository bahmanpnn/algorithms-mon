
"""

[1,3,5,6],3 ==>1
[1,3,5,6],4 ==>2
[1,3,5,6],7 ==>4
[1,3,5,6],0 ==>0
[1,3,3,5,6],4 ==>3

"""

def search_insert(array,val):
    low=0
    high=len(array)-1 #4
    mid=high//2 #2

    while low <=high: #0<=4 #0<=1 #0<=0
        if val >array[mid]: #3>3? #3>3? #3>1=true
            mid+=1 #mid=0+1=1
            low=mid #low=1
        else:
            mid-=1 #2-1=1 #1-1=0
            high=mid #high=1 high=0
    
    return low


print(search_insert([1,3,3,5,6],4))