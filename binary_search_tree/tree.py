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

    # Time Complexity: o(log n)
    # Space Complexity: o(log n)
    def add(self, key, value = None):
        if self.root ==None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: o(log n)
    # Space Complexity: o(1)
    def find(self, key):
        if self.root == None:
            return None
    
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key < key:
                    current = current.right
            else:
                    current = current.left

    # Time Complexity: o(n)
    # Space Complexity: o(n)
    def inorder(self):
        result = []
        return self.inorder_helper(self.root, result)
    
    def inorder_helper(self, current, result):
        
        if current == None:
            return result
        else:
            if current.left != None:
                self.inorder_helper(current.left, result)

            result.append({"key": current.key, "value" : current.value})
            
            if current.right != None:
                self.inorder_helper(current.right, result)
        
        return result

    # Time Complexity: o(n)
    # Space Complexity: o(n) 
    def preorder(self):
        result = []
        return self.preorder_helper(self.root, result)
    
    def preorder_helper(self, current, result):
        if current == None:
            return result
        else:
            result.append({"key": current.key, "value" : current.value})

            if current.left != None:
                self.preorder_helper(current.left, result)

            if current.right != None:
                self.preorder_helper(current.right, result)
        
        return result

    # Time Complexity: o(n)
    # Space Complexity: o(n)
    def postorder(self):
        result = []
        return self.postorder_helper(self.root, result)
    
    def postorder_helper(self, current, result):
        if current == None:
            return result
        else:
            if current.left != None:
                self.postorder_helper(current.left, result)
            if self.root.right != None:
                self.postorder_helper(current.right, result)
            result.append({"key": current.key, "value" : current.value})
        return result

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
                return self.height_helper(self.root) 
    
    def height_helper(self, current):
        if current == None:
            return 0
        
        return self.find_max(self.height_helper(current.left), self.height_helper(current.right))+1

    def find_max(self, a, b):
        if(a>=b):
            return a
        else:
            return b


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
