'''
# [1,2,1,3,4,5,2] ==[1,2]
return number that exist more in arr;if 2 or more numbers exist equal more in arr return all

'''
def top_one(arr):
    values={}
    result=[]
    f_val=0

    for item in arr:
        if item in values:
            values[item]+=1
        else:
            values[item]=1
    f_val=max(values.values())

    for key in values.keys():
        if values[key]==f_val:
            result.append(key)

    return result

arr=[1,2,1,3,4,5,2]
print(top_one(arr))