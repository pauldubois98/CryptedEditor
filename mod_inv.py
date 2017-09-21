def mod_inv(e, n):
    """returns the inverse of e mod n"""
    q=[]
    r=[]
        
    r0=n%e
    a=n
    b=e
    q.append(a)
    r.append(a)
    q.append(a)
    r.append(b)
    q.append(int(a/b))
    r.append(a%b)
    
    while r0!=0:
        a=b
        b=r0
        r0=a%b
        q.append(int(a/b))
        r.append(a%b)



    
    if r[len(r)-2]!=1:
        raise Exception('Modular inverse does not exists')
    else:
        l=len(r)
        t=[0,1]
        for i in range(2, l-2):
            t.append(t[i-2]-q[i]*t[i-1])

        d=t[l-4]-q[l-2]*t[l-3]
        while d<0:
            d+=n
        return d







if __name__=='__main__':
    #to be done if principal program
    while True:
        try:
            a=mod_inv(int(input("e?")), int(input("n?")))
        except:
            pass
        else:
            print("e-1 mod n is:", a)

    
