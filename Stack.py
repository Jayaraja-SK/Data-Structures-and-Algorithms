class Stack:
    def __init__(self):
        self.stack=list()

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if(self.is_empty()):
            print("STACK IS EMPTY")
            return
        
        self.stack.pop()

    def display(self):
        if(self.is_empty()):
            print("STACK IS EMPTY")
            return
        
        for i in range(len(self.stack)-1,-1,-1):
            print("|    ",self.stack[i],"    |")

    def top(self):
        if(self.is_empty()):
            print("STACK IS EMPTY")
            return
        print(self.stack[-1])

    def is_empty(self):
        if(len(self.stack)==0):
            return True
        return False

if __name__=="__main__":
    
    print("-"*60)
    print(f'\t\t\tSTACK')
    print("-"*60)
    print()

    obj=Stack()
    choice=0
    while(True):
        print("-"*50)
        print("\t\t\tMENU")
        print("-"*50)
        print("1. PUSH")
        print("2. POP")
        print("3. DISPLAY")
        print("4. TOP")
        print("5. IS EMPTY")
        print("6. EXIT")
        choice=int(input("ENTER CHOICE="))
        print()
        if choice==1:
            val=int(input("ENTER ITEM TO BE INSERTED="))

            print("\nBEFORE")
            obj.display()
            print()
            
            obj.push(val)

            print("AFTER")
            obj.display()

        elif choice==2:
            print("\nBEFORE")
            obj.display()
            print()
            
            obj.pop()

            print("AFTER")
            obj.display()

        elif choice==3:
            obj.display()

        elif choice==4:
            obj.top()

        elif choice==5:
            print(obj.is_empty())

        elif choice==6:
            break

        else:
            print("INVALID CHOICE")


        print("\n")
