class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def set_data(self,data):
        self.data=data

    def get_data(self):
        return self.data

    def set_left(self,node):
        self.left=node

    def get_left(self):
        return self.left

    def set_right(self,node):
        self.right=node

    def get_right(self):
        return self.right
    

class BST:
    def __init__(self,data=None):
        if(data is None):
            self.root=None
        else:
            self.root=data
        
    def insert(self,data):
        if(self.root is None):
            self.root=Node(data)
        else:
            if(self.root.data > data):
                if(self.root.get_left() is not None):
                    BST(self.root.get_left()).insert(data) #REFERENCES TO NEW SUB-TREE
                else:
                    self.root.set_left(Node(data))
            if(self.root.data < data):
                if(self.root.get_right() is not None):
                    BST(self.root.get_right()).insert(data)
                else:
                    self.root.set_right(Node(data))
        
    def search(self,data,level):
        if(self.root is not None):
            if(self.root.data == data):
                print(f'\nELEMENT FOUND AT LEVEL = {level}')
            elif(self.root.data > data):
                if(self.root.get_left() is None):
                    print(f'\nITEM NOT FOUND')
                else:
                    BST(self.root.get_left()).search(data,level+1)
            elif(self.root.data < data):
                if(self.root.get_right() is None):
                    print(f'\nITEM NOT FOUND')
                else:
                    BST(self.root.get_right()).search(data,level+1)
        else:
            print(f'\nITEM NOT FOUND')

    def delete(self,data):
        if(self.root is None):
            return None
        if(self.root.data > data):
            if(self.root.get_left() is not None):
                self.root.set_left(BST(self.root.get_left()).delete(data))
        elif(self.root.data < data):
            if(self.root.get_right() is not None):
                self.root.set_right(BST(self.root.get_right()).delete(data))
        else:
            if(self.root.get_left() and self.root.get_right()):
                left_max=BST(self.root.get_left()).find_max().get_data()
                self.root.set_data(left_max)
                self.root.set_left(BST(self.root.get_left()).delete(left_max))
            elif(self.root.get_left()):
                self.root=self.root.get_left()
            elif(self.root.get_right()):
                self.root=self.root.get_right()
            else:
                self.root=None

        return self.root

    def find_max(self):
        if(self.root is None):
            return None

        if(self.root.get_right() is None):
            return self.root
        else:
            return BST(self.root.get_right()).find_max()

    def find_min(self):
        if(self.root is None):
            return None

        if(self.root.get_left() is None):
            return self.root
        else:
            return BST(self.root.get_left()).find_min()

    def preorder(self): # PARENT-LEFT-RIGHT
        print(self.root.data)

        if(self.root.get_left() is not None):
            BST(self.root.get_left()).preorder()

        if(self.root.get_right() is not None):
            BST(self.root.get_right()).preorder()            

    def inorder(self): # LEFT-PARENT-RIGHT
        if(self.root.get_left() is not None):
            BST(self.root.get_left()).inorder()

        print(self.root.data)
        
        if(self.root.get_right() is not None):
            BST(self.root.get_right()).inorder()
            
    def postorder(self): # LEFT-RIGHT-PARENT
        if(self.root.get_left() is not None):
            BST(self.root.get_left()).postorder()

        if(self.root.get_right() is not None):
            BST(self.root.get_right()).postorder()

        print(self.root.data)

        
            

if __name__=="__main__":
    
    print("-"*60)
    print(f'\t\t\tBINARY SEARCH TREE')
    print("-"*60)
    print()

    obj=BST()
    
    choice=0
    while(True):
        print("-"*50)
        print("\t\t\tMENU")
        print("-"*50)
        print("1. INSERT")
        print("2. SEARCH")
        print("3. DELETE")
        print("4. FIND MIN")
        print("5. FIND MAX")
        print("6. PRE-ORDER TRAVERSAL")
        print("7. IN-ORDER TRAVERSAL")
        print("8. POST-ORDER TRAVERSAL")
        print("9. EXIT\n")
        choice=int(input("ENTER CHOICE="))
        print()
        if choice==1:
            val=int(input("ENTER ITEM TO BE INSERTED="))

            obj.insert(val)

            print(f'\nITEM INSERTED SUCCESSFULLY')

        elif choice==2:
            val=int(input("ENTER ITEM TO BE SEARCHED="))
            
            obj.search(val,0)

        elif choice==3:
            val=int(input("ENTER ITEM TO BE DELETED="))

            obj.delete(val)

            print(f'\nITEM DELETED SUCCESSFULLY')

        elif choice==4:
            print(f'MINIMUM ELEMENT IN TREE = {obj.find_min().data}')

        elif choice==5:
            print(f'MAXIMUM ELEMENT IN TREE = {obj.find_max().data}')

        elif choice==6:
            obj.preorder()

        elif choice==7:
            obj.inorder()

        elif choice==8:
            obj.postorder()

        elif choice==9:
            break

        else:
            print("INVALID CHOICE")

        print("\n")
        
        
