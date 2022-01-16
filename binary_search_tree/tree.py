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

    def add_helper(self, current_node, key, value): 
        if current_node == None: 
            return TreeNode(key, value)
        if key <= current_node.key: 
            current_node.left = self.add_helper(current_node.left, key, value)
        else: 
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def add(self, key, value = None):
        if self.root == None: 
            self.root = TreeNode(key, value)
        else: 
            self.add_helper(self.root, key, value)

    def find_helper(self, current_node, key):
        if current_node == None: 
            return None
        elif current_node.key == key: 
            return current_node.value
        elif current_node.key <= key: 
            return self.find_helper(current_node.right, key) 
        return self.find_helper(current_node.left, key) 

    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def find(self, key):
        if self.root == None: 
            return None
        else: 
            return self.find_helper(self.root, key)

    def inorder_helper(self, current, traversal_list): 
        if current != None: 
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append({"key":current.key,"value":current.value})
            self.inorder_helper(current.right, traversal_list)

    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def inorder(self):
        traversal_list = [] 
        self.inorder_helper(self.root, traversal_list)
        return traversal_list

    def preorder_helper(self, current, traversal_list): 
        if current != None: 
            traversal_list.append({"key":current.key,"value":current.value})
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity:  O(N)
    # Space Complexity: O(N)  
    def preorder(self):
        traversal_list = [] 
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, traversal_list): 
        if current != None: 
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append({"key":current.key,"value":current.value})

    # Time Complexity: O(N)
    # Space Complexity: O(N)  
    def postorder(self):
        traversal_list = [] 
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    def height_helper(self, current):
        if current is None:
            return 0
        return 1+max(self.height_helper(current.left), self.height_helper(current.right))

    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def height(self):
        return self.height_helper(self.root)



#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
