def trip():
    k= int(input())
    l=[]
    l1=[]
    s=[]
    for i in range(0,k):
        ele=int(input())
        l.append(ele)

    for j in range(0,len(l)):
        for k in range(1,len(l)):
            for f in range(2,len(l)):
                if l[j]+l[k]+l[f]==0:
                    s=(l[j],l[k],l[f])
                    l1.append(s)
    print(l1)
    print("No of triplet: ",len(l1))
trip()
