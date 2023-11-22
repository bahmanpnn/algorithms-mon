"""
    is morphic
    foo, bar ==>false {f:b,o:a,o:r} (b,a,r)
    foo, bee ==>true  {f:b,o:e}     (b,e,e)
    fow, bee ==>false {f:b,o:e,w:e} (b,e,e)
    paper,title ==> true {p:t,a:i,p:t,e:l,r:e} (t,i,t,l,e)
"""

def is_morphic(s,t):
    
    if len(s) != len(t):
        return False #it is checking the len of both strings and if they are not equal return false 
    
    dict={}
    set_values=set()

    for i in range(len(s)):
        if s[i] not in dict:

            if t[i] in set_values:
                return False #it is checking second strings word that is in set values or not
            
            dict[s[i]]=t[i]
            set_values.add(t[i])
        
        else:
            if dict[s[i]] !=t[i]:
                return False

    # {f:b,o:e,o:e} ==>o is key and cant use twice in dictionary so it will be ==>{f:b,o:e}
    # return dict,set_values

    return True

print(is_morphic("foo","bee"))
# print(is_morphic("foo","bar"))
# print(is_morphic("fow","bee"))
# print(is_morphic("paper","title"))

