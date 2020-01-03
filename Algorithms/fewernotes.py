def noofnotes(n):
    a=0
    s=[]
    l=[1000,500,100,50,10,5,2,1]
    for i in range(0,len(l)):
        k=int(n/l[i])
        a+=k
        s.append(k)
        n=n%l[i]
        if n==1:
            break
    print("No of notes :",a)
    for j in range(0,len(s)):
        if s[j]>0:
            print("Rs",l[j] ,"-",s[j])

n=int(input("amount in Rs."))

noofnotes(n)
