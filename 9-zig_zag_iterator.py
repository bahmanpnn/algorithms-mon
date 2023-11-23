"""
[1,3,5,7,9] , [2,4,6,8,10] ==> 1,2,3,4,5,6,7,8,9,10

[[1,3,5,7,9] , [2,4,6,8,10]]==>[[2,4,6,8,10][3,5,7,9]] ,1
[[3,5,7,9] , [4,6,8,10]] ==>1,2
...
...
[[],[]]==>1,2,3,4,5,6,7,8,9,10

"""

class ZigZag:
    
    def __init__(self,l1,l2):
        self.queue=[l1,l2]
    
    def next(self):
        v=self.queue.pop(0)
        r=v.pop(0)
        if v:
            self.queue.append(v)
        return r
    
    def has_next(self):
        if self.queue:
            return True
        return False
    
z=ZigZag([1,3,5,7,9] , [2,4,6,8,10] )

print(z.queue)
while z.has_next():
    print(z.next(),end=' ')
print(z.queue)