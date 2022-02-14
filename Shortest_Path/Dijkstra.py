import math

def Size(edges): # NO. OF EDGES IN A GRAPH
    vertices=set()
    
    for i in range(0,len(edges)):
        vertices.add(edges[i][0])
        vertices.add(edges[i][1])

    return len(vertices)


def Matrix(directed_edges): # ADJACENCY MATRIX OF A GRAPH
    edges=directed_edges+[(j,i,w) for (i,j,w) in directed_edges] # UN-DIRECTED
    
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
    edges=directed_edges+[(j,i,w) for (i,j,w) in directed_edges] # UN-DIRECTED
    
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



def Dijkstra_Matrix(WMat,s): # DIJKSTRA USING ADJACENCY MATRIX
    visited,distance=dict(),dict()

    for i in range(0,len(WMat)):
        visited[i]=False
        distance[i]=math.inf

    distance[s]=0


    for i in range(0,len(WMat)):
        min_d=math.inf

        for j in range(0,len(WMat)):
            if(visited[j] is False and min_d>distance[j]):
                min_d=distance[j]

        next_v=-1

        for j in range(0,len(WMat)):
            if(visited[j] is False and min_d==distance[j]):
                next_v=j

        if(next_v==-1):
            break

        visited[next_v]=True

        for j in range(0,len(WMat[i])):
            if(WMat[next_v][j][0]==1 and visited[j] is False):
                distance[j]=min(distance[j],distance[next_v]+WMat[next_v][j][1])

    return distance


def Dijkstra_List(WList,s): # DIJKSTRA USING ADJACENCY LIST
    visited,distance=dict(),dict()

    for i in WList.keys():
        visited[i]=False
        distance[i]=math.inf

    distance[s]=0

    for i in range(0,len(WList.keys())):
        min_d=math.inf

        for j in WList.keys():
            if(visited[j] is False and min_d>distance[j]):
                min_d=distance[j]

        next_v=-1

        for j in WList.keys():
            if(visited[j] is False and min_d==distance[j]):
                next_v=j

        if(next_v==-1):
            break

        visited[next_v]=True

        for (v,d) in WList[next_v]:
            if(visited[v] is False):
                distance[v]=min(distance[v],distance[next_v]+d)

    return distance


if __name__=="__main__": # NOTE - POSSIBLE VERTICES = {0,1,2...}
    
    directed_edges=[(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]

    WMat=Matrix(directed_edges)

    WList=Adj_List(directed_edges)

    src_vertex=0
    
    

    print(f'DIJKSTRA USING ADJACENCY MATRIX\n')

    res=Dijkstra_Matrix(WMat,src_vertex)

    for i in res:
        print(f'{src_vertex} - {i} = {res[i]}')
        
        

    print(f'\nDIJKSTRA USING ADJACENCY LIST\n')

    res=Dijkstra_List(WList,src_vertex)

    for i in res:
        print(f'{src_vertex} - {i} = {res[i]}')
