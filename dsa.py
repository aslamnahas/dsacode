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

ll1=Linked_list()
# s=[1,2,3,4]
ll1.add_first(10)
ll1.end_add(22)
ll1.add_first(111)
ll1.end_add(9)
ll1.add_first(2)

ll1.printt()