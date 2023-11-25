"""
    this algorithm is working with random key for every char of text and save that keys in list
    to use again for decryption
    
    **i think it is better to use dictionary for this algorithm and dont take keys and ciphers apart!

    bahman ==>ord(b)+randint(+*/-)... , ... ==>key=[number,...],cipher=[number,...]
    
"""
import random

class OneTimePadCipher:
    
    def encrypt(self,text):
        
        plain=[ord(i)for i in text]
        keys=[]
        cipher=[]
        for i in plain:
            k=random.randint(1,255)
            # c=(i+k)*k
            c=(i+k)
            cipher.append(c)
            keys.append(k)

        return cipher,keys
    
    def decrypt(self,cipher,keys):

        plain=[]
        for i in range(len(keys)):
            # char=int((cipher[i]-keys[i] **2)/ keys[i])
            char=int(cipher[i]-keys[i])
            plain.append(chr(char))

        # result=''.join([i for i in plain])
        result=''.join(i for i in plain)
        return result

ciphersss,keysss=OneTimePadCipher().encrypt('bahman')
print("cipher is =",ciphersss,'\t','keys are = ',keysss)

print("text is= ",OneTimePadCipher().decrypt(ciphersss,keysss))