def days(m,d,y):
    y1=y-(14-m)/12
    x=y1+y1/4-y1/100+y1/400
    k=12*x
    m1 = m+k*((14-m)/12)-2
    m2 = 31*m1
    d1 = ((d+x+m2)/12)
    d2 = d1%7
    if (d2==0):
        print "Sunday"
    elif d2==1:
        print "Monday"
    elif d2==2:
        print "Tuesday"
    elif d2==3:
        print "Wednesday"
    elif d2==4:
        print "Thursday"
    elif d2==5:
        print "Friday"
    elif d2==6:
        print "Saturday"
m=input()
d=input()
y=input()
days(m,d,y)
