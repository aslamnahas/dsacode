class Node:
    def __init__(self,data):
        self.data =data
        self.ref = None

class Linked_list:
    def __init__(self):
        self.head=None
    def printt(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None: 
                print(n.data,'--->',end=" ")
                n = n.ref
                # print(n)

    def add_first(self,data):
        new_noode = Node(data)
        new_noode.ref= self.head
        self.head = new_noode
    def end_add(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode





    def add_middle(self,data,x):
        n=self.head
        while n is not None:

            if n.data==x:
                break
                
            n= n.ref
        if n is None:
            print("node is not in this linked list")
        else:
            new_node =Node(data)
            new_node.ref=n.ref
            n.ref = new_node

    def middlechck(self,data,x):
        if self.head is None:
            print('the list is empkty')
        
        if self.head.data==x:
            newnode=Node(data)
            newnode.ref=self.head
            self.head=newnode
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print(f"Node with data {x} is not in the linked list")
        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode

    def middleaddbefore(self,data,x):
         if self.head is None:
             print("List is empty")
             return
        
         if self.head.data==x:
            newnode=Node(data)
            newnode.ref=self.head
            self.head=newnode
            return
         n = self.head
         while n.ref is not None:
             if n.ref.data == x:
                 break
             n = n.ref
         if n.ref is None:
            print(f"Node with data {x} is not in the linked list")
         else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode

    def middle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.ref is not None:
            slow = slow.ref
            fast = fast.ref.ref
        return slow.data

    def deletefirst(self):
        if self.head is None:
            print('there is empty')
        else:
            self.head=self.head.ref

    def enddelete(self):
        if self.head is None:
            print('nonnnnnenenenennene')
        # elif self.head.ref is None:
        #         self.head=None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def middledelte(self, x):
        if self.head is None:
            print('no node ')
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
            
                break
            n = n.ref
        if n.ref is None:
            print('lllllllllllll')
        else:

            n.ref = n.ref.ref
        
            

  
ll1=Linked_list()
# s=[1,2,3,4]

# ll1.add_first(10)
# for i in s:
    # ll1.end_add(i)
# ll1.end_add(22)


# ll1.middlechck(15, 2)

# ll1.printt()
# ll1.add_first(111)
# ll1.end_add(9)
# ll1.add_middle(102,3)
# ll1.add_middle(102,3)
ll1.add_first(2)
ll1.add_first(22)
ll1.add_first(209)
# ll1.deletefirst()
# ll1.middle()
# ll1.enddelete()
ll1.middledelte(209)
ll1.printt()
# print()
# ll1.middleaddbefore(100,2)
# ll1.printt()
# a = ll1.middle()
# print('midleee',a)