# min=3 ==>3,4,5,6
# max =3 ==>1,2,3
# min=3 ,max=3 ==> 3


def limit(list,max=None,min=None):
    min_checker=lambda val:True if min is None else (val >=min)
    max_checker=lambda val:True if max is None else (val <=max)

    return [val for val in list if min_checker(val) and max_checker(val)]

def simple_limit(arr,max=None,min=None):
    if min and max is not None:

        both_list=[]
        for val in arr:
            if val>=min and val<= max:
                both_list.append(val)
        
        return both_list
        
    else:
        if min is not None:
            list=[]
            for val in arr:
                if val >=min:
                    list.append(val)
                else:
                    continue
            return list
    
        if max is not None:
            list=[]
            for val in arr:
                if val <= max:
                    list.append(val)
                else:
                    continue
            return list



arr=[1,2,3,4,5,6]

print(limit(arr,min=2,max=4))
# print(limit(arr,min=3,max=3))

# print(simple_limit(arr,min=2,max=4))
# print(simple_limit(arr,min=3,max=3))