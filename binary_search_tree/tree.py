class TreeNode:
    def __init__(self, key, value = None):
        if value == None:
            value = key

        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n) if balanced
    # Space Complexity: O(1)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
    
    def add_helper(self, current, key, value):
        if current == None:
            return TreeNode(key, value)
        if current.key > key:
            current.left = self.add_helper(current.left, key, value)
        else:
            current.right = self.add_helper(current.right, key, value)
        return current 

    # Time Complexity: O(log n) if balanced
    # Space Complexity: O(1)
    def find(self, key):
        return self.find_helper(self.root, key)

    def find_helper(self, current, key):
        if current == None:
            return None
        if current.key == key:
            return current.value
        elif current.key > key:
            return self.find_helper(current.left, key)
        else:
            return self.find_helper(current.right, key)
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        tree_nodes = []
        if self.root == None:
            return tree_nodes
        return self.inorder_helper(self.root, tree_nodes)

    def inorder_helper(self, current, tree_nodes):
        if current == None:
            return

        #left
        self.inorder_helper(current.left, tree_nodes)

        #root
        tree_nodes.append({
            'key' : current.key,
            'value' : current.value
        })

        #right
        self.inorder_helper(current.right, tree_nodes)

        return tree_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(n)   
    def preorder(self):
        tree_nodes = []
        if self.root == None:
            return tree_nodes
        return self.preorder_helper(self.root, tree_nodes)

    def preorder_helper(self, current, tree_nodes):
        if current == None:
            return

        #root
        tree_nodes.append({
            'key' : current.key,
            'value' : current.value
        })

        #left
        self.preorder_helper(current.left, tree_nodes)

        #right
        self.preorder_helper(current.right, tree_nodes)

        return tree_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        tree_nodes = []
        if self.root == None:
            return tree_nodes
        return self.postorder_helper(self.root, tree_nodes)
    
    def postorder_helper(self, current, tree_nodes):
        if current == None:
            return

        #left
        current.left = self.postorder_helper(current.left, tree_nodes)

        #right
        current.right = self.postorder_helper(current.right, tree_nodes)

        #root
        tree_nodes.append({
            'key' : current.key,
            'value' : current.value
        })

        return tree_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(height of the tree?)  
    def height(self):
        return self.height_helper(self.root)
    
    def height_helper(self, current):
        if current == None:
            return 0
        left = self.height_helper(current.left)
        right = self.height_helper(current.right)
        max = left
        if right > max:
            max = right
        return max + 1

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
