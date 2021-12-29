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

    # Time Complexity: O(log n) if Balanced BST and O(n) for Unbalanced BST
    # Space Complexity: O(log n) if Balanced BST and O(1) for Unbalanced BST
    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        if current_node.key >= key:
            current_node.left = self.add_helper(current_node.left, key, value)
        elif current_node.key < key:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: O(log n) if Balanced BST and O(n) for Unbalanced BST
    # Space Complexity: O(log n) if Balanced BST and O(1) for Unbalanced BST
    def find_helper(self, current, key):
        if current == None:
            return None
        if key == current.key:
            return current.value
        elif key < current.key and current.left != None:
            return self.find_helper(current.left, key)
        elif key > current.key and current.right != None:
            return self.find_helper(current.right, key)

    def find(self, key):
        if self.root != None:
            return self.find_helper(self.root, key)

    # Time Complexity: O(n) where n is each visited node
    # Space Complexity: O(n) - O(h) for the call stack, where h is the height of the tree
    # Inorder  Traversal: Left - Root - Right
    def inorder_helper(self, current, ascending_nodes):
        if current == None:
            return None
        
        self.inorder_helper(current.left, ascending_nodes)
        ascending_nodes.append({"key": current.key, 
                                "value": current.value})
        self.inorder_helper(current.right, ascending_nodes)

    def inorder(self):
        if self.root == None:
            return []

        ascending_nodes = []
        self.inorder_helper(self.root, ascending_nodes)

        return ascending_nodes

    # Time Complexity: O(n) where n is each visited node
    # Space Complexity: O(n) - O(h) for the call stack, where h is the height of the tree
    # Preoder traversal: Root - Left - Right  
    def preorder_helper(self, current, preorder_nodes):
        if current == None:
            return None

        preorder_nodes.append({"key": current.key, 
                                "value": current.value})
        self.preorder_helper(current.left, preorder_nodes)
        self.preorder_helper(current.right, preorder_nodes)

    def preorder(self):
        if self.root == None:
            return []

        preorder_nodes = []
        self.preorder_helper(self.root, preorder_nodes)

        return preorder_nodes

    # Time Complexity: O(n) where n is each visited node
    # Space Complexity: O(n) - O(h) for the call stack, where h is the height of the tree
    # Postorder traversal: Left - Right - Root
    def postorder_helper(self, current, postorder_nodes):
        if current == None:
            return None
        
        self.postorder_helper(current.left, postorder_nodes)
        self.postorder_helper(current.right, postorder_nodes)
        postorder_nodes.append({"key": current.key, 
                                "value": current.value})

    def postorder(self):
        if self.root == None:
            return []

        postorder_nodes = []
        self.postorder_helper(self.root, postorder_nodes)

        return postorder_nodes

    # Time Complexity: O(log n) if Balanced BST and O(n) for Unbalanced BST
    # Space Complexity:  O(n) where n is the number of nodes in a given binary tree.
    def height_helper(self, current, current_height):
        if current == None:
            return current_height

        left_height = self.height_helper(current.left, current_height + 1)
        right_height = self.height_helper(current.right, current_height + 1)

        return max(left_height, right_height)

    def height(self):
        if self.root != None:
            return self.height_helper(self.root, 0)
        else:
            return 0

#   # Optional Method
#   # Time Complexity: O(n) where n is the number of nodes -1 except root
#   # Space Complexity: O(?)
    def bfs(self):
        if self.root == None:
            return []

        level_nodes = []
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            level_nodes.append({"key": current.key, 
                            "value": current.value})

        return level_nodes

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
