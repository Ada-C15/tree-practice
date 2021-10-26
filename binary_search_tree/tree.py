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

    # need helper function for add
    def add_helper(self, current_node, key, value):

        if current_node == None:
            return TreeNode(key, value)
        
        # traverse left subtree
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            # traverse right subtree
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(log n) if tree is balanced
    # Space Complexity: O(n) ?
    def add(self, key, value = None):
        
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)


    # Time Complexity: O(log n) if tree is balanced
    # Space Complexity: O(n) ?
    def find(self, key): 
        # search function in notebook

        if self.root == None:
            return None
        
        current_node = self.root
        # while current node exists!
        while current_node != None:
            # if current node's key == key we're trying to find
            if current_node.key == key:
                return current_node.value  
            # if key is smaller than current node's key -> traverse left subtree
            elif current_node.key > key:
                current_node = current_node.left
            # if key is larger than current node's key -> traverse right subtree
            else:
                current_node = current_node.right
        
        return None 

    # Time Complexity: O(n)
    # Space Complexity: Dependent on the size/height of tree, O(h)
    def inorder(self):
        
        tree_arr = []

        if self.root == None:
            return tree_arr
        
        return self.inorder_helper(self.root, tree_arr)
        

    # need helper function for inorder 
    def inorder_helper(self, current_node, tree_arr):

        # left, current, right

        if current_node == None:
            return 
        
        self.inorder_helper(current_node.left, tree_arr)

        tree_arr.append ({
            'key': current_node.key,
            'value': current_node.value
        })
        self.inorder_helper(current_node.right, tree_arr)

        return tree_arr
        
    # Time Complexity: O(n)
    # Space Complexity: Dependent on the size/height of tree, O(h)
    def preorder(self):
        
        tree_arr = []

        if self.root == None:
            return tree_arr

        return self.preorder_helper(self.root, tree_arr)

    # need helperr function for preorder
    def preorder_helper(self, current_node, tree_arr):

        # current, left, right

        if current_node == None:
            return 
        
        tree_arr.append ({
            'key': current_node.key,
            'value': current_node.value
        })

        self.preorder_helper(current_node.left, tree_arr)
        self.preorder_helper(current_node.right, tree_arr)

        return tree_arr


    # Time Complexity: O(n)
    # Space Complexity: Dependent on the size/height of tree, O(h)
    def postorder(self):
        
        tree_arr = []

        if self.root == None:
            return tree_arr
        
        return self.postorder_helper(self.root, tree_arr)

    # need helper function for postorder
    def postorder_helper(self, current_node, tree_arr):

        #  left, right, current

        if current_node == None:
            return
        
        self.postorder_helper(current_node.left, tree_arr)
        self.postorder_helper(current_node.right, tree_arr)

        tree_arr.append ({
            'key': current_node.key,
            'value': current_node.value
        })

        return tree_arr

    # Time Complexity: O(n)
    # Space Complexity: Dependent on the size/height of tree, O(h)
    def height(self):
        
        if self.root == None:
            return 0
        
        return self.height_helper(self.root)
        
    
    #  need helper function for height
    def height_helper(self, current_node):

        if current_node == None:
            return 0
        
        left = self.height_helper(current_node.left)
        right = self.height_helper(current_node.right)
        max = left

        if right > max:
            max = right
        return max + 1



#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass
        #  NOPE
        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
        #  NOPE