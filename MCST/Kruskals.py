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



def Kruskal(WList): # MINIMUM SPANNING TREE
    edges=list()
    comp=dict() # COMPONENTS ARE USED TO DETECT CYCLES IN A GRAPH
    TreeEdges=list()

    for u in WList.keys():
        for v in WList[u]:
            edges.append((v[1],u,v[0]))
        comp[u]=u

    edges.sort()


    for (d,u,v) in edges:
        if(comp[u]!=comp[v]):
            TreeEdges.append((u,v,d))
            c=comp[u]

            for w in WList.keys():
                if(comp[w]==c):
                    comp[w]=comp[v]

    return TreeEdges


if __name__=="__main__":
    directed_edges=[(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]

    WList=Adj_List(directed_edges)

    res=Kruskal(WList)

    print(f'RESULTANT MINUMUM SPANNING TREE USING KRUSKAL\'S ALGORITHM\n')

    for i in range(0,len(res)):
        print(f'EDGE = {res[i][0]}-{res[i][1]}  WEIGHT = {res[i][2]}')

