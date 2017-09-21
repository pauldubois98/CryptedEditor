from primeFunc import *
from encrypt import *


def code(file, txt, e, n):
    """function that crypt text with n and e, and save it in file"""
    l=make_cry_int(txt, e, n)

    #open
    f=open(file, 'w')

    #write n & e
    f.write(str(n)+'\n'+str(e)+'\n')

    #write the text
    for i in l:
        f.write(str(i)+' ')
        print(str(i)+' ')
    f.close()
    

    #close
    f.close()
    


def decode(file, password):
    """function that decode file with password"""
    f=open(file, 'r')
    text=f.read().split('\n')
    n=int(text[0])
    e=int(text[1])
    p, q, phi=getKeys(password)
    d=mod_inv(e, phi)
    return (uncode(text[2], d, n), p, q, n, phi, e, d)

def uncode(text, d, n):
    """function that uncode text with private key d and publik key n"""
    text1=text.split(' ')
    del text1[-1]
    for i in range(len(text1)):
        text1[i]=int(text1[i])
    s=make_decry_string(text1, d, n)
    return s

    
    
if __name__=='__main__':
    #to be exucuted if principle program
    code('try.txt', 'hello, how are you?', 7, 97*53)
    f=open('try.txt', 'r')
    text=f.read().split('\n')
    print(uncode(text[2], 4279, 97*53))
    
