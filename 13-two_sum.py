"""
    this algorithm is checking numbers in sequence to sum of two numbers equal to target that we give
    [2,7,1,11,15],18 ==>[1,3]
"""

def two_sum(numbers,target):
    p1=0
    p2=len(numbers)-1
    while p1<p2:
        s=numbers[p1]+numbers[p2]
        if s ==target:
            return [p1,p2]
        elif s>target:
            p2=p2-1
        else:
            p1=p1+1

print(two_sum([2,7,1,11,15],18))