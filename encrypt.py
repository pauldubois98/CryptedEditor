from fast import fast

def encrypt(m, e, n):
    """encrypting function"""
    return fast(m,e,n)

def decrypt(c, d, n):
    """decrypting function"""
    return fast(c,d,n)




def make_char(inte):
    """turn integers into the corresponding character"""
    return chr(inte)

def make_string(liste):
    """turn list of integers into the corresponding string"""
    s=''
    for i in liste:
        s+=make_char(i)
    return s

def make_decry_char(inte, d, n):
    """turn crypted integers into the corresponding character"""
    return chr(decrypt(inte, d, n))

def make_decry_string(liste, d, n):
    """turn list of pairs of crypted integers into the corresponding string"""
    s=''
    for i in liste:
        s+=make_decry_char(i, d, n)
    return s





def make_int(text1):
    """make pairs integers for each characters in text1"""
    l=[]
    for i in text1:
        l.append(ord(i))
    return l

def make_cry_int(text1, e, n):
    """make pairs integers for each characters in text1"""
    l=[]
    for i in text1:
        l.append(encrypt(ord(i), e, n))
    return l






if __name__=='__main__':
    ###to be executed if principle program
    ch='paul !'
    txt='Je suis le plus fort\net tout le monde le sait!!!'
    e=7
    d=4279
    p=97
    q=53
    n=p*q
    print('e=',e, '; d=',d, '; p=',p, '; q=',q, '; n=',n, '(=p*q)')
    print('texte1 =', ch)
    print('texte2 =', txt)
    print('')
    
    l=make_int(ch)
    print(l)
    #decrypatge 1
    print(make_string(l))

    lcry=make_cry_int(ch, e, n)
    print(lcry)
    #decrypatge 2
    print(make_decry_string(lcry, d, n))   




