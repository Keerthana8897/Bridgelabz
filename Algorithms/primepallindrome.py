def prime1():
    k=[]
    for val in range(2,1000+1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:

                k.append(val)
    l=[]
    for i in range(0,len(k)):
        if str(k[i])==str(k[i])[::-1]:
            l.append(k[i])

    print(l)
prime1()
