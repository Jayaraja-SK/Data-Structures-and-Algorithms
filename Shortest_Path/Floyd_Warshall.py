import math
import numpy as np

def Size(edges): # NO. OF EDGES IN A GRAPH
    vertices=set()
    
    for i in range(0,len(edges)):
        vertices.add(edges[i][0])
        vertices.add(edges[i][1])

    return len(vertices)


def Matrix(directed_edges): # ADJACENCY MATRIX OF A GRAPH
    edges=directed_edges

    for i in range(0,len(directed_edges)):
        edges.append([directed_edges[i][1],directed_edges[i][0],directed_edges[i][2]])
    
    size=Size(edges)

    WMat=list()

    for i in range(0,size):
        temp=list()
        
        for j in range(0,size):
            temp.append([0,0])

        WMat.append(temp)

    for (i,j,w) in edges:
        WMat[i][j][0]=1
        WMat[i][j][1]=w

    return WMat


def Adj_List(directed_edges): # ADJACENCY LIST OF A GRAPH
    edges=directed_edges

    for i in range(0,len(directed_edges)):
        edges.append([directed_edges[i][1],directed_edges[i][0],directed_edges[i][2]])
    
    size=Size(edges)
    
    WList=dict()

    for i in range(0,len(edges)):
        if(edges[i][0] not in WList):
            WList[edges[i][0]]=[[edges[i][1],edges[i][2]]]
        else:
            WList[edges[i][0]].append([edges[i][1],edges[i][2]])

    for i in range(0,size):
        if(i not in WList):
            WList[i]=list()

    return WList


def Floyd_Warshall(WMat):
    WMat=np.array(WMat)

    rows,cols,x=WMat.shape

    SP=np.zeros(shape=(rows,cols,cols+1)) # TRANSITIVE CLOSURE INITIALIZATION

    for i in range(0,rows): # SP^0 INITIALIZATION
        for j in range(0,cols):
            SP[i,j,0]=math.inf

    for i in range(0,rows): # SP^0 == WMat
        for j in range(0,cols):
            if(WMat[i,j,0]==1):
                SP[i,j,0]=WMat[i,j,1]

    for k in range(1,cols+1):
        for i in range(0,rows):
            for j in range(0,cols):
                SP[i,j,k]=min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[k-1,j,k-1])

    return SP[:,:,cols]


if __name__=="__main__":
    directed_edges=[(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]

    WMat=Matrix(directed_edges)

    res=Floyd_Warshall(WMat)

    print(f'SHOREST PATH BETWEEN EVERY PAIR OF VERTICES USING FLOYD WARSHALL\n')

    for i in range(0,len(res)):
        for j in range(i,len(res)):
            print(f'{i} TO {j}  DISTANCE = {res[i][j]}')
