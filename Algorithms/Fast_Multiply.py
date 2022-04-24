# KARATSUBA'S ALGORITHM

def fast_multiply(x,y,n): # COMPLEXITY - O(N^log(3))
    if(n==1):
        return x*y
    else:
        m=n//2

        x1,x0=x//(2**m),x%(2**m)
        y1,y0=y//(2**m),y%(2**m)
        a,b=x1-x0,y1-y0

        p=fast_multiply(x1,y1,m)
        q=fast_multiply(x0,y0,m)
        r=fast_multiply(a,b,m)

        return (p*(2**n))+((p+q-r)*(2**(n//2)))+q


A=12
B=13
N=4 # NO. OF BITS IN ITS BINARY REP.
print(fast_multiply(A,B,N))
