import random
import math
def flipacoin(n):
    sides=('head','tail')
    h=0
    t=0
    for i in range(0,n):
        s=random.choice(sides)
        print(s)
        if s=='head':
            h+=1
        else:
            t+=1
    perH=100.0*(float(h)/float(h+t))
    perL=100.0-perH
    print "head vs tail is",perH-perL
n=input()
flipacoin(n)
