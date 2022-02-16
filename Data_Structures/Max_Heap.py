class MaxHeap:
    def __init__(self):
        self.arr=list()

    def Max_Heapify(self,k):
        left=2*k+1
        right=2*k+2

        smallest=k

        if(left<len(self.arr) and self.arr[left]>self.arr[smallest]):
            smallest=left
        if(right<len(self.arr) and self.arr[right]>self.arr[smallest]):
            smallest=right
        if(smallest!=k):
            self.arr[k],self.arr[smallest]=self.arr[smallest],self.arr[k]
            self.Max_Heapify(smallest)
            

    def Heapify(self,L):
        for i in range(0,len(L)):
            self.arr.append(L[i])

        n=int((len(self.arr)//2)-1)

        for i in range(n,-1,-1):
            self.Max_Heapify(i)
            

    def Insert(self,value):
        self.arr.append(value)

        index=len(self.arr)-1

        while(index>0):
            parent=(index-1)//2

            if(self.arr[index]>self.arr[parent]):
                self.arr[index],self.arr[parent]=self.arr[parent],self.arr[index]
                index=parent
            else:
                break
            

    def Delete_Max(self):
        if(self.Is_Empty()):
            return None

        self.arr[0],self.arr[-1]=self.arr[-1],self.arr[0]
        value=self.arr.pop()

        self.Max_Heapify(0)

        return value
        

    def Is_Empty(self):
        if(len(self.arr)==0):
            return True

        return False


    def Display(self):
        if(self.Is_Empty()):
            print(f'HEAP IS EMPTY\n')
            return
        
        print(f'ELEMENTS IN HEAP')
        for i in range(0,len(self.arr)):
            print(f'{self.arr[i]}')
        print()



if __name__=="__main__":
    obj=MaxHeap()
    
    while(True):
        print("-"*40)
        print(f'\t\tMENU')
        print("-"*40)
        print(f'| 1. | ADD A LIST OF VALUES')
        print(f'| 2. | INSERT')
        print(f'| 3. | DELETE MAX')
        print(f'| 4. | DISPLAY')
        print(f'| 5. | EXIT')
        print("-"*40)
        print()

        choice=int(input("ENTER CHOICE = "))
        print()

        if(choice==1):
            L=list(map(int,input("ENTER LIST = ").split())) # ENTER INPUT AS - 1 2 3 4 5
            print()

            obj.Heapify(L)
            
            print(f'ELEMENTS ARE INSERTED IN HEAP\n')

            choice_1=input("DO YOU WANT TO DISPLAY (Y/N) = ")
            print()

            if(choice_1=='Y' or choice_1=='y'):
                obj.Display()
        elif(choice==2):
            val=int(input("ENTER VALUE TO BE INSERTED = "))
            print()

            obj.Insert(val)

            print(f'VALUE IS INSERTED\n')
        elif(choice==3):
            status=obj.Delete_Max()

            if(status is None):
                print(f'HEAP IS EMPTY\n')
            else:
                print(f'MAX. VALUE - {status} IS DELETED FROM HEAP\n')
        elif(choice==4):
            obj.Display()
        elif(choice==5):
            break
        else:
            print(f'INVALID CHOICE')
