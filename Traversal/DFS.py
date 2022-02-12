visited,parent=dict(),dict()

class Stack:
    def __init__(self):
        self.arr=list()

    def push(self,value):
        self.arr.append(value)

    def pop(self):
        if(self.isempty()):
            return

        return self.arr.pop()

    def top(self):
        if(self.isempty()):
            return

        return self.arr[-1]

    def isempty(self):
        if(len(self.arr)==0):
            return True

        return False


def DFSInit(AList):
    global visited,parent

    for i in AList.keys():
        visited[i]=False
        parent[i]=-1
        

def DFS(AList,v):
    global visited,parent
    
    visited[v]=True

    for i in AList[v]:
        if(not(visited[i])):
            parent[i]=v
            DFS(AList,i)

    return
    

if __name__=="__main__":
    AList={0: [1, 2, 4], 1: [0, 2], 2: [0, 1], 3: [4, 5, 6], 4: [0, 3, 7], 5: [3, 6, 7, 8], 6: [3, 5], 7: [4, 5, 8], 8: [5, 7, 9], 9: [8]}

    DFSInit(AList)

    DFS(AList,0)

    print(f'DEPTH FIRST SEARCH TRAVERSAL\n\n')

    print(f'PARENT-RELATION\n')

    for i in parent:
        print(f'NODE = {i} PARENT = {parent[i]}')
                
        
