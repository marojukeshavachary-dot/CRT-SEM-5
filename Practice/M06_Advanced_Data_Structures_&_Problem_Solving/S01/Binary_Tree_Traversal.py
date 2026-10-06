class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
        
#Tree Structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  
# Tree Travesal ==> DFS(pre_order, in-order, post_order), BFS(Level order)
def pre_order(root):
    if root:
        print(root.data,end="-->")
        pre_order(root.left)
        pre_order(root.right)
pre_order(root)