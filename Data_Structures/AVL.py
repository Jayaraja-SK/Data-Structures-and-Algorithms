class AVL:
    def __init__(self,init_val=None):
        self.value=init_val

        if(self.value is None):
            self.left=None
            self.right=None
            self.height=0
        else:
            self.left=AVL()
            self.right=AVL()
            self.height=1


    def is_empty(self):
        if(self.value is None):
            return True

        return False


    def Left_Rotate(self):
        dot=self.value
        dot_left=self.left
        diamond=self.right.value
        diamond_left=self.right.left
        diamond_right=self.right.right

        new_dot=AVL(dot)
        new_dot.left=dot_left
        new_dot.right=diamond_left

        self.value=diamond
        self.left=new_dot
        self.right=diamond_right


    def Right_Rotate(self):
        dot=self.value
        dot_right=self.right
        diamond=self.left.value
        diamond_left=self.left.left
        diamond_right=self.left.right

        new_dot=AVL(dot)
        new_dot.left=diamond_right
        new_dot.right=dot_right

        self.value=diamond
        self.left=diamond_left
        self.right=new_dot


    def Update_Height(self):
        if(self.is_empty()):
            return
        else:
            self.left.Update_Height()
            self.right.Update_Height()
            self.height=1+max(self.left.height,self.right.height)


    def Rebalance(self):
        if(self.left is None):
            h_l=0
        else:
            h_l=self.left.height

        if(self.right is None):
            h_r=0
        else:
            h_r=self.right.height

        if((h_l-h_r)>1):
            if(self.left.left.height>self.left.right.height):
                self.Right_Rotate()
            if(self.left.left.height<self.left.right.height):
                self.left.Left_Rotate()
                self.Right_Rotate()

            self.Update_Height()
            
        if((h_l-h_r)<-1):
            if(self.right.left.height<self.right.right.height):
                self.Left_Rotate()
            if(self.right.left.height>self.left.right.height):
                self.right.Right_Rotate()
                self.Left_Rotate()

            self.Update_Height()

        


    def Insert(self,v):
        if(self.is_empty()):
            self.value=v
            self.left=AVL()
            self.right=AVL()
            self.height=1

            return

        if(self.value==v):
            return
        elif(v<self.value):
            self.left.Insert(v)
            self.Rebalance()
            self.height=1+max(self.left.height,self.right.height)
            return 
        else:
            self.right.Insert(v)
            self.Rebalance()
            self.height=1+max(self.left.height,self.right.height)
            return


    def Inorder(self): # LEFT, NODE, RIGHT
        if(self.is_empty()):
            return ([])
        else:
            return (self.left.Inorder()+[self.value]+self.right.Inorder())


    def Preorder(self): # NODE, LEFT, RIGHT
        if(self.is_empty()):
            return ([])
        else:
            return ([self.value]+self.left.Preorder()+self.right.Preorder())


    def Postorder(self): # LEFT, RIGHT, NODE
        if(self.is_empty()):
            return ([])
        else:
            return (self.left.Postorder()+self.right.Postorder()+[self.value])


    def Min_Value(self):
        if(self.left.is_empty()):
            return self.value
        else:
            return self.left.Min_Value()


    def Max_Value(self):
        if(self.right.is_empty()):
            return self.value
        else:
            return self.right.Max_Value()


    def is_leaf(self): # CHECKS IF CURRENT NODE IS LEAF NODE OR NOT
        return (self.value!=None and self.left.is_empty() and self.right.is_empty())


    def Clear_Node(self): # DELETES LEAF NODE
        self.value=None
        self.left=None
        self.right=None


    def Copy_Left(self):
        self.value=self.left.value
        self.left=self.left.left
        self.right=self.left.right


    def Copy_Right(self):
        self.value=self.right.value
        self.left=self.right.left
        self.right=self.right.right


    def Delete(self,v):
        if(v<self.value):
            self.left.Delete(v)
            self.left.Rebalance()
        elif(v>self.value):
            self.right.Delete(v)
            self.left.Rebalance()
        elif(v==self.value):
            if(self.is_leaf()): # NODE IS LEAF
                self.Clear_Node()
            elif(self.left.is_empty()): # LEFT NODE IS EMPTY
                self.Copy_Right()
            elif(self.right.is_empty()): # RIGHT NODE IS EMPTY
                self.Copy_Left()
            else: # BOTH LEFT AND RIGHT NODES ARE NOT EMPTY
                self.value=self.left.Max_Value()
                self.left.Delete(self.left.Max_Value())


    

if __name__=="__main__":
    obj=AVL()
    
    while(True):
        print("-"*40)
        print(f'\t\tMENU')
        print("-"*40)
        print(f'| 1. | INSERT')
        print(f'| 2. | DELETE')
        print(f'| 3. | MIN. VALUE')
        print(f'| 4. | MAX. VALUE')
        print(f'| 5. | IN-ORDER')
        print(f'| 6. | PRE-ORDER')
        print(f'| 7. | POST-ORDER')
        print(f'| 8. | EXIT')
        print("-"*40)
        print()

        choice=int(input("ENTER CHOICE = "))
        print()

        if(choice==1):
            val=int(input("ENTER VALUE TO BE INSERTED = "))
            print()

            obj.Insert(val)

            print(f'VALUE IS INSERTED\n')
        elif(choice==2):
            val=int(input("ENTER VALUE TO BE DELETED = "))
            print()

            obj.Delete(val)
        elif(choice==3):
            print(f'MIN. VALUE IN TREE = {obj.Min_Value()}\n')
        elif(choice==4):
            print(f'MAX. VALUE IN TREE = {obj.Max_Value()}\n')
        elif(choice==5):
            res=obj.Inorder()

            print(f'IN-ORDER TRAVERSAL')

            for i in res:
                print(f'{i}')
            print()
        elif(choice==6):
            res=obj.Preorder()

            print(f'PRE-ORDER TRAVERSAL')

            for i in res:
                print(f'{i}')
            print()
        elif(choice==7):
            res=obj.Postorder()

            print(f'POST-ORDER TRAVERSAL')

            for i in res:
                print(f'{i}')
            print()
        elif(choice==8):
            break
        else:
            print(f'INVALID CHOICE')

