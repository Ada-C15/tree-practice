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
        

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
 
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        
        return None

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder_helper(self, current_node, inorder_list = []):
        if current_node == None:
            return inorder_list

        if current_node.left:
            self.inorder_helper(current_node.left, inorder_list)

        inorder_list.append({"key" : current_node.key, "value" : current_node.value})

        if current_node.right:
            self.inorder_helper(current_node.right, inorder_list) 
        
        return inorder_list

    def inorder(self):
        return self.inorder_helper(self.root)

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder_helper(self, current_node, preorder_list = []):
        if current_node == None:
            return preorder_list

        preorder_list.append({"key" : current_node.key, "value" : current_node.value})

        if current_node.left:
            self.preorder_helper(current_node.left, preorder_list)

        if current_node.right:
            self.preorder_helper(current_node.right, preorder_list) 

        return preorder_list 

    def preorder(self):
        return self.preorder_helper(self.root)

    # Time Complexity: O(n)
    # Space Complexity:O(n)

    def postorder_helper(self, current_node, postorder_list = []):
        if current_node == None:
            return postorder_list

        if current_node.left:
            self.postorder_helper(current_node.left, postorder_list)
        if self.root.right:
            self.postorder_helper(current_node.right, postorder_list)

        postorder_list.append({"key" : current_node.key, "value" : current_node.value})

        return postorder_list

    def postorder(self):
        return self.postorder_helper(self.root)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):
        if not self.root:
            return 0
        
        lTree = Tree()
        lTree.root = self.root.left
        rTree = Tree()
        rTree.root = self.root.right

        return max(lTree.height(), rTree.height()) + 1
    


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
