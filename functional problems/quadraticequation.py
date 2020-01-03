import cmath
def quad(a,b,c):
    d=((b**2)-(4*a*c))
    root1=(-b+cmath.sqrt(d))/(2*a)
    root2=(-b-cmath.sqrt(d))/(2*a)
    print(root1)
    print(root2)

a=float(input())
b=float(input())
c=float(input())
quad(a,b,c)
