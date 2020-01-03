def prime():
    k=[]
    for val in range(2,1000+1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:

                k.append(val)
    l=[]
    m=0
    for i in range(0,len(k)):
        for j in range(1,len(k)):
                if sorted(str(k[i]))==sorted(str(k[j])):
                    if str(k[i])!=str(k[j]):
                        l.append(k[i])
                        break


    print(l)
prime()
