def insort(l):
    for i in range(0,len(l)):
        key=l[i]
        j=i-1
    while j >= 0 and key < l[j] :
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = key
    return(l)
l=[2,7,5,9,4,1]
print(insort(l))
