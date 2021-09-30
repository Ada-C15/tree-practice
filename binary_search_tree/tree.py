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

    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def add_helper(self, current_node, key, value): 
        if current_node == None: 
            return TreeNode(key, value)


        if key <= current_node.key: 
            current_node.left = self.add_helper(current_node.left, key, value)
        else: 
            current_node.right = self.add_helper(current_node.right, key, value)
        
        return current_node

    def add(self, key, value = None):
        if self.root == None: 
            self.root = TreeNode(key, value)
        else: 
            self.add_helper(self.root, key, value)

    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def find_helper(self, current_node, key):
        if current_node == None: 
            return None
        elif current_node.key == key: 
            return current_node.value
        elif current_node.key <= key: 
            return self.find_helper(current_node.right, key) 
        
        return self.find_helper(current_node.left, key) 

    def find(self, key):
        if self.root == None: 
            return None
        else: 
            return self.find_helper(self.root, key)

    # Time Complexity: o(n)
    # Space Complexity: o(n)
    def inorder_helper(self, current, traversal_list): 
        if current != None: 
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append({"key":current.key,"value":current.value})
            self.inorder_helper(current.right, traversal_list)

    def inorder(self):
        traversal_list = [] 
        self.inorder_helper(self.root, traversal_list)
        return traversal_list

    # Time Complexity:  o(n)
    # Space Complexity: o(n)   
    def preorder_helper(self, current, traversal_list): 
        if current != None: 
            traversal_list.append({"key":current.key,"value":current.value})
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)


    def preorder(self):
        traversal_list = [] 
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    # Time Complexity: o(n)
    # Space Complexity: o(n)  
    def postorder_helper(self, current, traversal_list): 
        if current != None: 
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append({"key":current.key,"value":current.value})

    def postorder(self):
        traversal_list = [] 
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def get_height(self, current):
        if current is None:
            return 0
        return 1+max(self.get_height(current.left), self.get_height(current.right))

    def height(self):
        return self.get_height(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        
#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
