class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key
        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def dict(self):
        return {'key': self.key, 'value': self.value}
class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n) - If balanced - because you are not traveling through all nodes but instead, check if > than or smaller so you cut through half every time
    # Space Complexity: O(1)  building one new node only no matter how big tree is, it only increases by 1 
    def add(self, key, value = None):

        if not self.root:
            self.root = TreeNode(key, value)
            return
        parent = None 
        current = self.root
        while current:
            parent = current
            if key > current.key:
                current = current.right
            else:  
                current = current.left 
        if key <= parent.key:
            parent.left = TreeNode(key, value)
        else:
            parent.right = TreeNode(key, value)

    def add_helper(self, current_node, key, value):
        if not current_node:
            return TreeNode(key, value)
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:  
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(log n) - if balanced
    # Space Complexity: O(log n) - you are putting things on the stack for each level looked at
    def add_recursively(self, key, value = None):
        if not self.root:
            self.root = TreeNode(key, value)
            return
        self.add_helper(self.root, key, value)

    # Time Complexity: O(log n) - if balanced, O(n) if not balanced
    # Space Complexity: O(1) 
    def find(self, key):
        if not self.root:
            return None
        current = self.root
        while current:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_help(self, current_node, traversal_list):
        if current_node:

            self.inorder_help(current_node.left, traversal_list)
            traversal_list.append(current_node.dict())
            self.inorder_help(current_node.right, traversal_list)

    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def inorder(self):
        traversal_list = []
        self.inorder_help(self.root, traversal_list)
        return traversal_list
    
    def preorder_help(self, current_node, traversal_list):
        if current_node:
            traversal_list.append(current_node.dict())
            self.preorder_help(current_node.left, traversal_list)
            self.preorder_help(current_node.right, traversal_list)
        
    # Time Complexity: O(n) - traverses each node
    # Space Complexity: O(n)
    def preorder(self):
        traversal_list = []
        self.preorder_help(self.root, traversal_list)
        return traversal_list

    def postorder_help(self, current_node, traversal_list):
        if current_node:
            self.postorder_help(current_node.left, traversal_list)
            self.postorder_help(current_node.right, traversal_list)
            traversal_list.append(current_node.dict())

    # Time Complexity: O(n) - traverses each node
    # Space Complexity: O(n) - as big as list grows  
    def postorder(self):
        traversal_list = []
        self.postorder_help(self.root, traversal_list)
        return traversal_list
    
    def height_help(self, current_node):
        if not current_node:
            return 0
        height_left = self.height_help(current_node.left)
        height_right = self.height_help(current_node.right)
        return max(height_left, height_right) + 1
    
    # Time Complexity: O(n) 
    # Space Complexity: O(1)     
    def height(self):
        return self.height_help(self.root)

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
