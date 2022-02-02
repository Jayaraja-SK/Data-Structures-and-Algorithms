import math

def Size(edges): # NO. OF EDGES IN A GRAPH
    max_v=-1
    
    for i in range(0,len(edges)):
        max_v=max(max_v,max(edges[i][0],edges[i][1]))

    max_v=max_v+1

    return max_v


def Matrix(directed_edges): # ADJACENCY MATRIX OF A GRAPH
    edges=directed_edges
    
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
    
    size=Size(edges)
    
    WList=dict()

    for i in range(0,len(edges)):
        if(edges[i][0] not in WList):
            WList[edges[i][0]]=[[edges[i][1],edges[i][2]]]
        else:
            WList[edges[i][0]].append([edges[i][1],edges[i][2]])

    return WList


def Bellman_Ford_Matrix(WMat,s): # WMat - Weight Matrix
    distance=dict()

    for i in range(0,len(WMat)):
        distance[i]=math.inf

    distance[s]=0


    for i in range(0,len(WMat)): # To find the presence of cycle
        for j in range(0,len(WMat)):
            for k in range(0,len(WMat[j])):
                if(WMat[j][k][0]==1):
                    distance[k]=min(distance[k],distance[j]+WMat[j][k][1])

    return distance
                        


def Bellman_Ford_List(WList,s): # WList - Adjacency List
    distance=dict()

    for i in WList.keys():
        distance[i]=math.inf

    distance[s]=0


    for i in range(0,len(WList.keys())): # To find the presence of cycle
        for j in WList.keys():
            for (v,d) in WList[j]:
                distance[v]=min(distance[v],distance[j]+d)

    return distance
                        


if __name__=="__main__":
    
    directed_edges=[(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]

    WMat=Matrix(directed_edges)

    WList=Adj_List(directed_edges)

    src_vertex=0
    
    

    print(f'BELLMAN-FORD USING ADJACENCY MATRIX\n')

    res=Bellman_Ford_Matrix(WMat,src_vertex)

    for i in res:
        print(f'{src_vertex} - {i} = {res[i]}')
        
        

    print(f'\nBELLMAN-FORD USING ADJACENCY LIST\n')

    res=Bellman_Ford_List(WList,src_vertex)

    for i in res:
        print(f'{src_vertex} - {i} = {res[i]}')    
