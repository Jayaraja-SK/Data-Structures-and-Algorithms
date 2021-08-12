import collections

class Queue:
    def __init__(self):
        self.queue=collections.deque()

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        if(self.is_empty()):
            print("QUEUE IS EMPTY")
            return
        
        self.queue.popleft()

    def display(self):
        if(self.is_empty()):
            print("QUEUE IS EMPTY")
            return

        print("|",end=" ")
        for i in self.queue:
            print(i,end=" | ")
        print()

    def front(self):
        if(self.is_empty()):
            print("QUEUE IS EMPTY")
            return
        print(self.queue[0])

    def rear(self):
        if(self.is_empty()):
            print("QUEUE IS EMPTY")
            return
        print(self.queue[-1])

    def is_empty(self):
        if(len(self.queue)==0):
            return True
        return False

if __name__=="__main__":
    
    print("-"*60)
    print(f'\t\t\tQUEUE')
    print("-"*60)
    print()

    obj=Queue()
    choice=0
    while(True):
        print("-"*50)
        print("\t\t\tMENU")
        print("-"*50)
        print("1. ENQUEUE")
        print("2. DEQUEUE")
        print("3. DISPLAY")
        print("4. FRONT")
        print("5. REAR")
        print("6. IS EMPTY")
        print("7. EXIT")
        choice=int(input("ENTER CHOICE="))
        print()
        if choice==1:
            val=int(input("ENTER ITEM TO BE INSERTED="))

            print("\nBEFORE")
            obj.display()
            print()
            
            obj.enqueue(val)

            print("AFTER")
            obj.display()

        elif choice==2:
            print("\nBEFORE")
            obj.display()
            print()
            
            obj.dequeue()

            print("AFTER")
            obj.display()

        elif choice==3:
            obj.display()

        elif choice==4:
            obj.front()

        elif choice==5:
            obj.rear()

        elif choice==6:
            print(obj.is_empty())

        elif choice==7:
            break

        else:
            print("INVALID CHOICE")


        print("\n")
