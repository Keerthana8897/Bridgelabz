import random
import math
def gambler(S,G,T):
    h=0
    s=(0,1)
    for i in range(0,T):
        k=random.choice(s)
        if k==0:
            S-=1
        else:
            S+=1
            h+=1
        if S==G or S==0:
            break
    print "no of win:",h
    avg= (float(h)/float(T))*100
    print "avg:",avg
    print "no of bet:",T

S=input()
G=input()
T=input()
gambler(S,G,T)
