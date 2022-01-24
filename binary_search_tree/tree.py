'''the node stores a key value pair 
    with the key being how we are sorting and the value being the data
    '''
class TreeNode: 
    def __init__(self, key, value = None):
        # if the value is none the key will be the value
        # this allows the tree to just be a tree of integers
        if value == None:
            value = key

        self.key = key
        self.value = value
        self.left = None
        self.right = None
        

## tree class with a __init__ function
class Tree:
    def __init__(self):
        self.root = None
    
    def add_helper(self, current, key, value):
        if not current:
            return TreeNode(key,value)

        if key <= current.key:
            current.left = self.add_helper(current.left,key,value)
        else:
            current.right = self.add_helper(current.right,key,value)
        return current


    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key,value)
        else:
            self.add_helper(self.root, key,value)

        


    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None
        


    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        tree_nodes = []
        return self.inorder_helper(self.root, tree_nodes)

    def inorder_helper(self, root, tree_nodes):
        if root:
            self.inorder_helper(root.left, tree_nodes)
            tree_nodes.append({
                "key":root.key,
                "value":root.value
            })
            self.inorder_helper(root.right, tree_nodes)
        return tree_nodes


    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        tree_nodes = []
        return self.preorder_helper(self.root, tree_nodes)

    def preorder_helper(self, root, tree_nodes):
        if root:
            tree_nodes.append({
                "key":root.key,
                "value":root.value
            })
            self.preorder_helper(root.left, tree_nodes)
            self.preorder_helper(root.right, tree_nodes)
        return tree_nodes



    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        tree_nodes = []
        return self.postorder_helper(self.root, tree_nodes)

    def postorder_helper(self, root, tree_nodes):
        if root:
            self.postorder_helper(root.left, tree_nodes)
            self.postorder_helper(root.right, tree_nodes)
            tree_nodes.append({
                "key":root.key,
                "value":root.value
            })
        return tree_nodes

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        return self.height_helper(self.root)
    
    def height_helper(self, current):
        if not current:
            return 0

        left = self.height_helper(current.left)
        right = self.height_helper(current.right)
        return max(left, right)+1

        


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"


