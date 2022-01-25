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


    def add_helper(self, current_node, new_node):
        
        if current_node.key > new_node.key:
            if current_node.left == None:
                current_node.left = new_node
            else:
                self.add_helper(current_node.left, new_node)
        else:
            if current_node.right == None:
                current_node.right = new_node
            else:
                self.add_helper(current_node.right, new_node)
         
    
    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):

        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            new_node = TreeNode(key, value)
            self.add_helper(self.root, new_node)    


    def find_helper(self, current_node, key):
        
        if current_node == None:
            return None

        if current_node.key == key:
            return current_node

        if current_node.key > key:
            return self.find_helper(current_node.left, key)
        else:
            return self.find_helper(current_node.right, key)


    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        return self.find_helper(self.root, key).value


    def inorder_helper(self, current_node, inorder_return):
        if current_node == None:
            return inorder_return

        self.inorder_helper(current_node.left, inorder_return)
        inorder_return.append({ 
            "key": current_node.key,
            "value": current_node.value
        })
        self.inorder_helper(current_node.right, inorder_return)

        return inorder_return 
        
    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        inorder_return = []
        return self.inorder_helper(self.root, inorder_return)


    def preorder_helper(self, current_node, preorder_return):
        if current_node == None:
            return preorder_return

        preorder_return.append({ 
            "key": current_node.key,
            "value": current_node.value
        })
        self.preorder_helper(current_node.left, preorder_return)        
        self.preorder_helper(current_node.right, preorder_return)

        return preorder_return

    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        preorder_return = []
        return self.preorder_helper(self.root, preorder_return)


    def postorder_helper(self, current_node, postorder_return):
        if current_node == None:
            return postorder_return

        self.postorder_helper(current_node.left, postorder_return)        
        self.postorder_helper(current_node.right, postorder_return)
        postorder_return.append({ 
            "key": current_node.key,
            "value": current_node.value
        })

        return postorder_return

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        postorder_return = []
        return self.postorder_helper(self.root, postorder_return)


    def height_helper(self, current_node):
        if current_node == None:
            return 0
        
        left_node = self.height_helper(current_node.left)
        right_node = self.height_helper(current_node.right)

        return max(left_node, right_node) + 1

    # Time Complexity: 
    # Space Complexity:     
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
