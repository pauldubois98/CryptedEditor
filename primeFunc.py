from math import sqrt, log
from mod_inv import mod_inv
from random import randrange

def listPrime(maxi):
    """return a list of the primes less then maxi"""
    l=[True for i in range(maxi)]
    l[0], l[1]=False, False
    p=[]
    for a in range(2,int(sqrt(maxi-1))):
        if l[a]:
            p.append(a)
            for i in range (a*a,maxi,a):
                if l[i]==1:
                    l[i]=False
    for a in range(int(sqrt(maxi-1)), maxi):
        if l[a]:
            p.append(a)
    return p

def randPrime(maxi):
    """give a prime less then maxi, at random"""
    l=listPrime(maxi)
    return l[randrange(len(l))]


def isPrime(n):
    """tels if n is prime"""
    r=True
    for i in listPrime(int(sqrt(n))):
        if n%i==0:
            r=False
    return r

def nextPrime(n):
    """return first prime number gerater or equal to n"""
    while isPrime(n)==False:
        n+=1
    return n
    

def newKeys(password):
    """create new keys from password"""
    p, q, phi=getKeys(password)
    n=p*q
    
    e=randPrime(int(log(phi)))
    ex=True
    while ex:
        try:
            d=mod_inv(e, phi)
        except:
            ex=True
            e=randPrime(int(log(phi)))
        else:
            ex=False
    return (p, q, n, phi, e, d)


def getKeys(password):
    """generate keys p and q from password"""
    password1=password[:int(len(password)/2)]
    password2=password[int(len(password)/2):]
    p=1
    for i in password1:
        p*=ord(i)
    q=1
    for i in password2:
        q*=ord(i)
    
    p=nextPrime(p)
    q=nextPrime(q)
    phi=p*q-p-q+1
    return (p, q, phi)












if __name__=='__main__':
    ###to be done if principle program
    for i in range(1, 10):
        print(randPrime(1000))
    
