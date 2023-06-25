# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ==>ascii_letters
# bahman,key=2==>dcjocp

from string import ascii_letters

def encrypt(string,key=3):
    alpha=ascii_letters
    result=''

    for char in string:
        if char not in alpha:
            result+=char
        else:
            new_char=(alpha.index(char)+key)%len(alpha)
            result+=alpha[new_char]

    return result

def decrypt(string,key):
    key*=-1
    return encrypt(string,key)

# ------------------------------------------------------- brute_force
# with brute_force can try all the key indexes to check what key is true with test and shifting keys and decrypt strings!

def brute_force(string):
    alpha=ascii_letters
    result=''
    key=1
    brute_force_data={}

    while key<=len(alpha):
        result=decrypt(string,key)
        brute_force_data[key]=result
        result=''
        key+=1
    return brute_force_data


print(encrypt('bahman',2))
print('_________________')
print(decrypt('dcjocp',2))
print('_________________')
print(brute_force('dcjocp'))



