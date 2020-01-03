def binary2(x):
    q=x
    s=''
    for i in range(0,x):

        if q%2 >=1:
            s+='1'
        else:
            s+='0'
        if q<=1:
            break
        q=q/2
    print s[-1::-1]

x=input()
binary2(x)
