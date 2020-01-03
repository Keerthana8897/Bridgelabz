def findno(n,c):
    l=[]
    for i in range(0,n):
        a=2**i
        l.append(a)
    e=len(l)
    print(l)

    while(e!=0):
        mid=int(len(l)/2)
        print(mid)
        if l[mid]==c:
            print("true")
            break
        elif mid<=0:
            print("false")
            break
        elif l[mid]>c:
           e=mid
           l=l[:e]
        elif l[mid]<c:
            s=mid
            l=l[s:]
        else:
            if mid<=0:
                print("false")
                break


n=int(input())
c=int(input())
findno(n,c)
