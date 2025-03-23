import result
import logging
logger = logging.getLogger(__name__)



class Node:
    #constructor used to initialise attributes for objects to be created
    def __init__(self,data):
        logger.info("creating a node")
        self.data = data
        #next points to none
        self.next = None
class Linked_List:
    
    def __init__(self,head:Node):
        self.head = head


    def size_of_list(self):
        logger.info("Entering size_of_list")
        size = 0
        if self.head == None:
            print("the size is 0 ")
            logger.error("The list only has head")
            logger.info("Exiting size_of_list")
        else:
            a = self.head
            index = 0
            while a is not None:
                a = a.next
                size+=1
                logger.info("Exiting size of list")
                print("the size is:",size)
                return size
         
          

    def traverse_list(self)->result.ret_val:
        logger.info("entering traverse list")
        if self.head == None:
            print("the linked list is empty and the head is :",self.head)
            logger.error("Head is empty")
            logger.info("Exiting list")
        else:
            a = self.head
            index = 0
            while a is not None:
                print(a.data , end=" ")
                a = a.next
                index+=1
        logger.info("Exited list")
        ret = result.ret_val("success","traversed successfully",index)
        return ret
        
    
    

    def list_prepend(self,data):
        logger.info("Entering list_prepend")
        print("\n Entering list_prepend")        
        if data == None:
                print("Passed data is None")
                ret = result.ret_val("error","prepended failed",-1)
                print("\n Exiting list_prepend with error") 
                logger.error("No value was passed")
                logger.info("Exiting list_prepend")
                return ret
            
            
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        ret = result.ret_val("success","Prepend happend successfully",1)
        print("\n Exiting list_prepend") 
        logger.info("Exiting list_prepend")
        return ret
                
                
    def list_append(self,data):
                    logger.info("Entering list_append")
                    new_last_node = Node(data)
                    a = self.head 
                    while a.next is not None:
                        a = a.next
                    a.next = new_last_node
                    logger.info("Exiting list_append")
                    print("appending done")
                    ret = result.ret_val("success","appended successfully",self.size_of_list())

    def list_insert_at(self,data,index):
                    logger.info("Entering list_insert_at")
                    new_node = Node(data)
                    a = self.head
                    i = 1
                    size = self.size_of_list()
                    if index > size :
                        logger.error("The given exceeds the size of list")
                        ret = result.ret_val("error","inserting unsuccessful",-1)
                        logger.info("Exiting list_insert_at")
                        return ret

                    elif index == 0:
                        logger.info("The index is 0 , prepending")
                        self.list_prepend(data)
                        ret = result.ret_val("success","inserted at 0",0)
                        logger.info("Exiting list_insert_at")
                        return ret


                    for i in range(1,index-1):
                        a = a.next
                    new_node.next = a.next
                    a.next = new_node
                    ret = result.ret_val("success","inserted successfully at : ",1)
                    logger.info("Exiting list_insert_at")
                    return ret

    def list_delete_node(self,position):
                    logger.info("Entering list_delete_node")
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
                    logger.info("Exiting list_delete_node")
                    return ret

    def list_delete_head(self):
            logger.info("Entering list_delete_head")
            a = self.head
            self.head = a.next
            a.next = None
            print()
            ret = result.ret_val("success","deleted successfully at : ",1)
            logger.info("Exiting list_delete_head")
            return ret

    def list_delete_end(self):
            logger.info("Entering list_delete_end")
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
            logger.info("Exiting list_delete_end")
            return ret

    def list_reverse(self):
            logger.info("Entering list_reverse")
            prev = None
            current = self.head
            while current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev
            logger.info("Exiting list_reverse")

    def display_list(self):
            logger.info("Entering display_list")
            first = self.head
            while(first):
                print (first.data,end=" ")
                first = first.next
            logger.info("Exiting display_list")