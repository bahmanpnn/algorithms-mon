"""
    this algorithm is working on string and get a number as parametr
    to pop first of string as much as parametr and add end of the string
    
    "hello",2 ==> llohe
    "hello",5 ==> hello 
    "hello",6 ==> elloh  
    "hello",7 ==> llohe
"""

def rotate(s,k):
    if isinstance(s,str):
        double_s=s+s #bahmanbahman
        if k<=len(s):
            return double_s[k:k+len(s)]
        else:
            return double_s[k-len(s):k] #[25-6:25] ==>return '' and does not have error!!
    else:
        return s
    
print(rotate("bahman",25))
# print(rotate("bahman",4))
# print(rotate("bahman",7))