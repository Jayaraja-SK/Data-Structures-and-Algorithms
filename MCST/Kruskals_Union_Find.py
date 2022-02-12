import math


comp=dict()
members=dict()
size=dict()


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


def MakeUnionFind(WList):
    global comp,members,size

    for i in WList.keys():
        comp[i]=i
        members[i]=[i]
        size[i]=1


def Find(i):
    global comp
    
    return comp[i]


def Union(i,j):
    global comp,members,size
    
    c_old=comp[i]
    c_new=comp[j]

    for k in members[c_old]:
        comp[k]=c_new
        members[c_new].append(k)
        size[c_new]=size[c_new]+1


def Kruskal(WList): # WITH REDUCED COMPLEXITY USING UNION-FIND
    edges=list()
    TreeEdges=list()

    MakeUnionFind(WList) # COMPONENTS HAVE BEEN DEFINED IN SEPARATE FUNCTION

    global comp,members,size

    for u in WList.keys():
        for v in WList[u]:
            edges.append((v[1],u,v[0]))

    edges.sort()


    for (d,u,v) in edges:
        if(Find(u)!=Find(v)):
            TreeEdges.append((u,v,d))

            Union(comp[u],comp[v])

    return TreeEdges



directed_edges=[(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]

WList=Adj_List(directed_edges)

res=Kruskal(WList)

print(f'RESULTANT MINUMUM SPANNING TREE\n')

for i in range(0,len(res)):
    print(f'EDGE = {res[i][0]}-{res[i][1]}  WEIGHT = {res[i][2]}')

