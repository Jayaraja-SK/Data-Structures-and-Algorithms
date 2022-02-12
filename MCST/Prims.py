import math

def Size(edges): # NO. OF EDGES IN A GRAPH
    vertices=set()
    
    for i in range(0,len(edges)):
        vertices.add(edges[i][0])
        vertices.add(edges[i][1])

    return len(vertices)


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


def Prims(WList):
    visited,distance,TreeEdges=dict(),dict(),list()

    for u in WList.keys():
        visited[u]=False
        distance[u]=math.inf

    visited[0]=True # NEED NOT BE 0TH VERTEX. ANY VERTEX CAN BE CHOSED

    for v,d in WList[0]:
        distance[v]=d

    for i in WList.keys():
        min_d=math.inf
        next_vertex=None

        for u in WList.keys():
            for v,d in WList[u]:
                if(visited[u] and not(visited[v]) and min_d>d):
                    min_d=d
                    next_vertex=v
                    next_edge=(u,v,d)

        if(next_vertex is None):
            break

        visited[next_vertex]=True
        TreeEdges.append((next_edge))

        for (v,d) in WList[next_vertex]:
            if(not(visited[v])):
                distance[v]=min(distance[v],d)

    return TreeEdges
            
            
if __name__=="__main__":
    directed_edges=[(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]

    WList=Adj_List(directed_edges)

    res=Prims(WList)

    print(f'RESULTANT MINUMUM SPANNING TREE USING PRIM\'S ALGORITHM\n')

    for i in range(0,len(res)):
        if(res[i]!=-1):
            print(f'EDGE = {res[i][0]}-{res[i][1]} WEIGHT = {res[i][2]}')

