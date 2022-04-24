def MoM(L): # EFFICIENT METHOD TO FIND MEDIAN IN A LIST (MEDIAN OF MEDIANS)
    if(len(L)<=5):
        L.sort()
        return L[len(L)//2]

    M=list()

    for i in range(0,len(L),5):
        X=L[i:i+5]
        X.sort()
        M.append(X[len(X)//2])

    return MoM(M)


def fast_select(L,l,r,k): # TO FIND KTH SMALLEST ELEMENT IN LIST
    if(k<1 or k>r-l):
        return None

    pivot=MoM(L[l:r]) # MEDIAN

    for i in range(l,r):
        if(pivot==L[i]):
            pivot_pos=i
            break

    L[l],L[pivot_pos]=L[pivot_pos],L[l] # MOVE MEDIAN TO 1ST POSITION

    pivot,lower,upper=L[l],l+1,l+1

    for i in range(l+1,r):
        if(L[i]>pivot):
            upper=upper+1
        else:
            L[i],L[lower]=L[lower],L[i]
            lower=lower+1
            upper=upper+1


    L[l],L[lower-1]=L[lower-1],L[l]
    lower=lower-1

    lowerlen=lower-l

    if(k<=lowerlen):
        return fast_select(L,l,lower,k)
    elif(k==lowerlen+1):
        return L[lower]
    else:
        return fast_select(L,lower+1,r,k-(lowerlen+1))


L=[5,3,4,1,2]
k=2

res=fast_select(L,0,len(L),k)

print(f'KTH SMALLEST ELEMENT IN LIST = {res}')
            
