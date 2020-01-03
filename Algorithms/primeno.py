def prime(n):
    for val in range(2,n+1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                print(val)
n=input()
prime(n)
