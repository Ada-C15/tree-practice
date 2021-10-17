class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    def add(self, key, value=None):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    def add_helper(self, current_node, key, value):
        if current_node is None:
            return TreeNode(key, value)

        if key < current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)

        return current_node


    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    def find(self, key):
        return self.find_helper(self.root, key)

    def find_helper(self, current, key):
        if current is None:
            return None

        if current.key == key:
            return current.value
        if current.key > key:
            return self.find_helper(current.left, key)

        return self.find_helper(current.right, key)
            


    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def inorder(self):
        return self.inorder_helper(self.root)

    def inorder_helper(self, current):
        order = []
        if current:
            order = self.inorder_helper(current.left)
            order.append({'key': current.key, 'value': current.value})
            order = order + self.inorder_helper(current.right)
        return order


    # Time Complexity: O(n) 
    # Space Complexity: O(n)     
    def preorder(self):
        return self.preorder_helper(self.root)

    def preorder_helper(self, current):
        order = []
        if current:
            order.append({'key': current.key, 'value': current.value})
            order = order + self.preorder_helper(current.left)
            order = order + self.preorder_helper(current.right)

        return order


    # Time Complexity: O(n) 
    # Space Complexity: O(n)    
    def postorder(self):
        return self.postorder_helper(self.root)

    def postorder_helper(self, current):
        order = []
        if current:
            order = self.postorder_helper(current.left)
            order = order + self.postorder_helper(current.right)
            order.append({'key': current.key, 'value': current.value})
        
        return order

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, current):
        height = 0

        if current:
            height = 1 + max(self.height_helper(current.left), self.height_helper(current.right))

        return height

    # Optional Method/Breadth-First Search
    # Time Complexity: 
    # Space Complexity: 
    def bfs(self):
        return self.bfs_helper(self.root)

    def bfs_helper(self, current):

        if not self.root:
            return []

    # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
