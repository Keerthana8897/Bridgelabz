import math
def monthlypay(P,Y,R):
    n=12*Y
    r=R/(12*100)
    k=P*r
    h=1-(1+r)**(-n)
    pay=float(k)/float(h)
    print pay
P=input()
Y=input()
R=input()
monthlypay(P,Y,R)
