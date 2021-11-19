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

    # Time Complexity: O(log n) *if balanced
    # Space Complexity: O(1)
    def add(self, key, value = None):
        # edge case: if tree is empty, add node at root
        if self.root == None:
            self.root = TreeNode(key, value)
            return None
        # find the parent node
        else:
            parent = None
            curr_node = self.root
            while curr_node != None:
                parent = curr_node
                if key < curr_node.key:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

        # determine on which side of the node to create the node   
        if key < parent.key:
            parent.left = TreeNode(key, value)
        else:
            parent.right = TreeNode(key, value) 

    def add_helper(self, curr_node, key, value):
        if curr_node == None:
            return TreeNode(key, value)

        if key < curr_node.key:
            curr_node.left = self.add_helper(curr_node.left, key, value)
        else:
            curr_node.right = self.add_helper(curr_node.right, key, value)
        return curr_node

    # Time Complexity: O(log n) *if balanced
    # Space Complexity: O(log n) *if balanced
    def add_recursive(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            # use helper method to add parameter
            self.add_helper(self.root, key, value)
        

    # Time Complexity: O(log n) *if balanced
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        
        curr_node = self.root
        while curr_node != None:
            if curr_node.key == key:
                return curr_node.value
            elif key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None
    
    def find_helper(self, curr_node, key, value):
        if curr_node == None:
            return None
        
        if key < curr_node.key:
            curr_node.left = self.find_helper(curr_node.left, key, value)
        else:
            curr_node.right = self.find_helper(curr_node, key, value)
        return curr_node
    
    # Time Complexity: O(log n) *if balanced
    # Space Complexity: O(log n) *if balanced
    def find_recursive(self, key, value = None):
        if self.root == None:
            return None
        else:
            self.find_helper(self.root, key, value)
        
    def preorder_helper(self, curr_node, trav_list):
        if curr_node == None:
            return 
        else:
            trav_list.append({"key": curr_node.key, "value": curr_node.value})
            self.preorder_helper(curr_node.left, trav_list)
            self.preorder_helper(curr_node.right, trav_list)

    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def preorder(self):
        if self.root == None:
            return []
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def inorder_helper(self, curr_node, trav_list):
        if curr_node == None:
            return
        else:
            self.inorder_helper(curr_node.left, trav_list)
            trav_list.append({"key": curr_node.key, "value": curr_node.value})
            self.inorder_helper(curr_node.right, trav_list)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        if self.root == None:
            return []
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, curr_node, trav_list):
        if curr_node == None:
            return
        else:
            self.postorder_helper(curr_node.left, trav_list)
            self.postorder_helper(curr_node.right, trav_list)
            trav_list.append({"key": curr_node.key, "value": curr_node.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def postorder(self):
        if self.root == None:
            return []
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    def height_helper(self, curr_node):
        if curr_node == None:
            return 0
        left_height = self.height_helper(curr_node.left)
        right_height = self.height_helper(curr_node.right)
        return max(left_height, right_height) + 1

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def height(self):
        if self.root == None:
            return 0
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        if self.root == None:
            return []
        queue = [self.root]
        bfs_list = []

        while len(queue) > 0:
            curr_node = queue.pop(0)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            bfs_list.append({"key": curr_node.key, "value": curr_node.value})
            
        return bfs_list

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
