class BTreeNode :
    def __init__(self,leaf=False):
        #the leaf is initialliy "False" because it is unclear whether the node would divide itself later
        self.leaf = leaf
        self.keys = []
        self.child = []
        self.order
class BTree :
    def __init__(self,order):
        self.root = BTreeNode(order,leaf=True)
        self.order =  order
    