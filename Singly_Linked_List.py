class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

    def setData(self,value):
        self.data=value
        
    def getData(self):
        return self.data

    def setNext(self,val):
        self.next=val

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head=None
        
    def addFirst(self,data):
        new=Node(data)
        new.setNext(self.head)
        self.head=new

    def addLast(self,data):
        if(self.head==None):
            self.addFirst(data)
            return
            
        new=Node(data)

        end=self.head
        while(end.next):
            end=end.getNext()
        end.next=new

    def size(self):
        count=0
        start=self.head
        while start is not None:
            count=count+1
            start=start.getNext()
        return count
    
    def insert(self,pos,val):
        if pos > self.size():
            print("\nENTERED POSITION HAS CROSSED THE LIMIT\n")
            return
        start=self.head
        pre=None

        if pos==0: #ADD AT FIRST
            self.addFirst(val)
        else:
            new=Node(val)
            incr=0
            while incr < pos:
                incr=incr+1
                pre=start
                start=start.getNext()
            pre.setNext(new)
            new.setNext(start)

    def remove(self,val):
        pre=None
        start=self.head
        while start:
            if start.getData() == val:
                if pre:
                    pre.setNext(start.getNext())
                else:
                    self.head=start.getNext()
                print("VALUE IS REMOVED")
                return True
            pre=start
            start=start.getNext()
        print("VALUE IS NOT FOUND") 
        return False

    def display(self):
        start=self.head
        if start is None:
            print("NO ELEMENTS IN LIST")
            return
        while start is not None:
            print(start.getData(),end=" ")
            start=start.getNext()
        print()

    def first(self):
        start=self.head
        if start is None:
            print("NO ELEMENTS IN LIST")
            return
        while start is not None:
            print(start.getData())
            break

    def tail(self):
        start=self.head
        if start is None:
            print("NO ELEMENTS IN LIST")
            return
        while start is not None:
            if start != self.head:
                print(start.getData(),end=" ")
            start=start.getNext()
        print()

    def sort(self):  #BUBBLE SORT
        temp=self.head
        new=Node(None)

        if temp is None:
            print("NO ELEMENTS IN LIST")
            return

        while temp is not None:
            new=temp.next

            while new is not None:
                if(temp.data > new.data):
                    temp.data,new.data=new.data,temp.data

                new=new.next
            temp=temp.next
            

if __name__=="__main__":
    
    print("-"*60)
    print(f'\t\t\tLINKED LIST')
    print("-"*60)
    print()

    obj=LinkedList()
    choice=0
    while(True):
        print("-"*50)
        print("\t\t\tMENU")
        print("-"*50)
        print("1. ADD AT FIRST")
        print("2. INSERT AT ANY GIVEN POSITION")
        print("3. ADD AT LAST")
        print("4. REMOVE")
        print("5. DISPLAY")
        print("6. HEAD")
        print("7. TAIL")
        print("8. SORT")
        print("9. EXIT")
        choice=int(input("ENTER CHOICE="))
        print()
        if choice==1:
            val=int(input("ENTER ITEM TO BE INSERTED="))

            print("\nBEFORE - ",end=" ")
            obj.display()

            obj.addFirst(val)

            print("AFTER  - ",end=" ")
            obj.display()
            print()

        elif choice==2:
            val=int(input("ENTER ITEM TO BE INSERTED="))
            pos=int(input("ENTER INDEX FOR INSERTION="))

            print("\nBEFORE - ",end=" ")
            obj.display()
            
            obj.insert(pos,val)

            print("AFTER  - ",end=" ")
            obj.display()

        elif choice==3:
            val=int(input("ENTER ITEM TO BE INSERTED="))

            print("\nBEFORE - ",end=" ")
            obj.display()

            obj.addLast(val)

            print("AFTER  - ",end=" ")
            obj.display()
            print()

        elif choice==4:
            val=int(input("ENTER ITEM TO BE REMOVED="))

            print("\nBEFORE - ",end=" ")
            obj.display()
            
            obj.remove(val)

            print("AFTER  - ",end=" ")
            obj.display()

        elif choice==5:
            obj.display()

        elif choice==6:
            obj.first()

        elif choice==7:
            obj.tail()

        elif choice==8:
            print("\nBEFORE - ",end=" ")
            obj.display()
            
            obj.sort()

            print("AFTER  - ",end=" ")
            obj.display()

        elif choice==9:
            break

        else:
            print("INVALID CHOICE")

        print("\n")
        
        
