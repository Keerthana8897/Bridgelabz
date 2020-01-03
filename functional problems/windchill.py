import math
def windchill(t,v):
   k=0.6215*t
   h=0.4275*t
   s=v**0.16
   w=35.74+k+(h-35.75)*s
   print(w)

t=input()
v=input()
windchill(t,v)
