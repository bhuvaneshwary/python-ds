#initialising class node 
import result
import list
import logging
logger = logging.getLogger(__name__)



def main():

    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    
    
    logger.info('Started')

    sll = list.Linked_List(list.Node(5))
    n2 = list.Node(10)
    sll.list_prepend(3)
    ret = sll.traverse_list()
    print(ret.message)
    sll.list_append(5)
    sll.traverse_list()
    sll.list_delete_node(1)
    sll.traverse_list()
    sll.list_reverse()
    print("reversed list : ")
    sll.display_list()
    r = sll.list_insert_at(4,2)
    print(r.message,r.index)
   
    #n = sll.list_delete_head()
   # print(n.message,n.index,n.status)
    sll.display_list()

    m = sll.list_delete_end()
    print(m.status,m.message,m.index)
    b = sll.list_delete_node(2)
    print(b.message,b.index)
if __name__ == "__main__":
    main()
    print(__name__)




