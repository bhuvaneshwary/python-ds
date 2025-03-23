import unittest
import list


class test_function(unittest.TestCase):
    def test_list_prepend(self):
        l=list.Linked_List(list.Node(23))
        r = l.list_prepend(2)
        self.assertEqual(r.status,"success")
    def test_list_nulldata(self):
        l=list.Linked_List(list.Node(None))
        r = l.list_prepend(None)
        self.assertEqual(r.status,"error")
    def test_list_insert_at_invalid_index(self):
        l = list.Linked_List(list.Node(100))
        r = l.list_insert_at(3,41000)
        self.assertEqual(r.index,-1)
    def test_list_insert_at_valid_index(self):
        l = list.Linked_List(list.Node(3))
        r = l.list_insert_at(4,1)
        self.assertEqual(r.index,1)
    def test_list_insert_at_zero_index(self):
        l = list.Linked_List(list.Node(3))
        r = l.list_insert_at(4,0)
        self.assertEqual(r.index,0)
    def test_list_delete_node(self):
        l = list.Linked_List(list.Node(3))
        r = l.list_insert_at(4,11)
        self.assertEqual(r.status,1)
    
    





if __name__ == '__main__':
    unittest.main()