"""
    this algorithm tries to find best profit in sequences.if there is no profit must return 0
    [7,1,5,3,6,4] ==> 5
    [9,7,6,4,3,1] ==> 0
"""
def max_profit(prices_list):
    current_max,max_so_far=0,0
    for i in range(1,len(prices_list)):
        current_max=max(0,current_max+prices_list[i]-prices_list[i-1])
        max_so_far=max(max_so_far,current_max)
    
    return max_so_far

print(max_profit([9,7,6,4,3,1]))