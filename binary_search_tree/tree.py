class TreeNode:
    def __init__(self, key, val=None):
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
        if current_node.key > key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_helper(self, root, elements):
        if root == None:
            return

        self.inorder_helper(root.left, elements)
        elements.append({"key": root.key, "value": root.value})
        self.inorder_helper(root.right, elements)
        return

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        if self.root == None:
            return []

        elements = []
        self.inorder_helper(self.root, elements)

        return elements

    def preorder_helper(self, root, elements):
        if root == None:
            return

        elements.append({"key": root.key, "value": root.value})
        self.preorder_helper(root.left, elements)
        self.preorder_helper(root.right, elements)
        return elements

    # Time Complexity: O(n)
    # Space Complexity: O(n)   
    def preorder(self):
        if self.root == None:
            return []

        elements = []
        self.preorder_helper(self.root, elements)
        return elements

    def postorder_helper(self, root, elements):
        if root == None:
            return

        self.postorder_helper(root.left, elements)
        self.postorder_helper(root.right, elements)
        elements.append({"key": root.key, "value": root.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        if self.root == None:
            return []
        elements = []
        self.postorder_helper(self.root, elements)
        return elements

    def height_helper(self, node):
        if not node:
            return 0

        left = self.height_helper(node.left)
        right = self.height_helper(node.right)

        return max(left, right) + 1

    # Time Complexity: O(n)
    # Space Complexity: O(log n)  
    def height(self):
        if self.root == None:
            return 0

        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
