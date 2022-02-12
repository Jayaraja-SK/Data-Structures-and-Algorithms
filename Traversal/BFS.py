import collections

class Queue:
    def __init__(self):
        self.arr=collections.deque()

    def addq(self,value):
        self.arr.append(value)

    def delq(self):
        if(self.isempty()):
            return

        return self.arr.popleft()

    def isempty(self):
        if(len(self.arr)==0):
            return True

        return False


def BFSListPathLevel(AList,v):
    level,parent=dict(),dict()

    for i in AList.keys():
        level[i]=-1
        parent[i]=-1

    q=Queue()

    level[v]=0

    q.addq(v)

    while(not(q.isempty())):
        j=q.delq()

        for k in AList[j]:
            if(level[k]==-1):
                level[k]=level[j]+1
                parent[k]=j
                q.addq(k)

    return (level,parent)


if __name__=="__main__":
    AList={0: [1, 2, 4], 1: [0, 2], 2: [0, 1], 3: [4, 5, 6], 4: [0, 3, 7], 5: [3, 6, 7, 8], 6: [3, 5], 7: [4, 5, 8], 8: [5, 7, 9], 9: [8]}

    level,parent=BFSListPathLevel(AList,0)

    print(f'BREADTH FIRST SEARCH TRAVERSAL\n\n')

    print(f'LEVEL-RELATION\n')

    for i in level.keys():
        print(f'NODE = {i} LEVEL = {level[i]}')

    print(f'\nPARENT-RELATION\n')
    
    for i in parent:
        print(f'NODE = {i} PARENT = {parent[i]}')
