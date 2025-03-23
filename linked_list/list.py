import result
class Node:
    #constructor used to initialise attributes for objects to be created
    def __init__(self,data):
        self.data = data
        #next points to none
        self.next = None
class Linked_List:
    
    def __init__(self,head:Node):
        self.head = head

    def traverse_list(self)->result.ret_val:
        if self.head == None:
            print("the linked list is empty and the head is :",self.head)
        else:
            a = self.head
            index = 0
            while a is not None:
                print(a.data , end=" ")
                a = a.next
                index+=1
        ret = result.ret_val("success","traversed successfully",index)
        return ret
    
    def size_of_list(self):
        size = 0
        if self.head == None:
            print("the size is 0 ")
        else:
            a = self.head
            index = 0
            while a is not None:
                a = a.next
                size+=1
            print("the size is:",size)
          

    def list_prepend(self,data):
            
        print("\n Entering list_prepend")        
        if data == None:
                print("Passed data is None")
                ret = result.ret_val("error","prepended failed",-1)
                print("\n Exiting list_prepend with error") 
                return ret
            
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        ret = result.ret_val("success","Prepend happend successfully",1)
        print("\n Exiting list_prepend") 
        return ret
                
                
    def list_append(self,data):
                    new_last_node = Node(data)
                    a = self.head 
                    while a.next is not None:
                        a = a.next
                    a.next = new_last_node
                    print("appending done")
                    #ret = result.ret_val("success","appended successfully",index)

    def list_insert_at(self,data,index):
                    new_node = Node(data)
                    a = self.head
                    i = 1
                    for i in range(1,index-1):
                        a = a.next
                    new_node.next = a.next
                    a.next = new_node
                    ret = result.ret_val("success","inserted successfully at : ",index)
                    return ret

    def list_delete_node(self,position):
                    prev = self.head
                    a = self.head.next
                    i =1
                    for i in range (1,position-1):
                        a = a.next
                        prev = prev.next
                    prev.next = a.next
                    a.next = None
                    print("deletion done")
                    ret = result.ret_val("success","deleted successfully at :",i)
                    return ret

    def list_delete_head(self):
            a = self.head
            self.head = a.next
            a.next = None
            print()
            ret = result.ret_val("success","deleted successfully at : ",1)
            return ret

    def list_delete_end(self):
            prev = self.head
            a = self.head.next
            size = 1
            while a.next is not None :
                    a = a.next
                    prev = prev.next
                    size+=1
                    
            print()
            prev.next = None
            ret = result.ret_val("success","deleted successfully",size)
            return ret

    def list_reverse(self):
            prev = None
            current = self.head
            while current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev

    def display_list(self):
            first = self.head
            while(first):
                print (first.data,end=" ")
                first = first.next