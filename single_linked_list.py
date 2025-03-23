#initialising class node 
class Node:
    #constructor used to initialise attributes for objects to be created
    def __init__(self,data):
        self.data = data
        #next points to none
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def traverse_list(self):
        if self.head == None:
            print("the linked list is empty and the head is :",self.head)
        else:
            a = self.head
            while a is not None:
                print(a.data , end=" ")
                a = a.next
    def list_prepend(self,data):
                new_head = Node(data)
                new_head.next = self.head
                self.head = new_head
    def list_append(self,data):
                new_last_node = Node(data)
                a = self.head 
                while a.next is not None:
                      a = a.next
                a.next = new_last_node
                print("appending done")
    def list_insert_at(self,data,index):
                new_node = Node(data)
                a = self.head
                for i in range(1,index-1):
                      a = a.next
                new_node.next = a.next
                a.next = new_node
    def list_delete_node(self,position):
                prev = self.head
                a = self.head.next
                for i in range (1,position-1):
                       a = a.next
                       prev = prev.next
                prev.next = a.next
                a.next = None
                print("deletion done")
    def list_delete_head(self):
           a = self.head
           self.head = a.next
           a.next = None
    def list_delete_end(self):
           prev = self.head
           a = self.head.next
           while a.next is not None :
                  a = a.next
                  prev = prev.next
           prev.next = None


n1 = Node(5)
sll = Linked_List()
sll.head  = n1
n2 = Node(10)
n1.next = n2
sll.list_prepend(3)
sll.traverse_list()
sll.list_append(5)
sll.traverse_list()
sll.list_delete_node(1)
sll.traverse_list()
