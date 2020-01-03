def harmonic(n):
    sum=0
    for i in range(1,n+1):

        if i ==n:
            print "1/", i
        else:
            print "1/", i ,"+",


n=input()
harmonic(n)
