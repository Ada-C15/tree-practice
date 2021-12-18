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
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add_helper(self, current, key, value):
        if current is None:
            return TreeNode(key, value)
        if current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        else:
            current.right = self.add_helper(current.right, key, value)
        return current
    
    def add(self, key, value = None):
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
            elif current.key > key:
                current = current.left
            else:
                current= current.right

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def inorder_helper(self, current, values_list):
        if not current: 
            return values_list
        object = {"key": current.key, "value": current.value}

        self.inorder_helper(current.left, values_list)
        values_list.append(object)
        self.inorder_helper(current.right, values_list)

        return values_list
    
    def inorder(self):
        values_list = []
        return self.inorder_helper(self.root, values_list)

    # Time Complexity: O(n)
    # Space Complexity: O(1)  

    def preorder_helper(self, current_node, values_list):
        if not current_node:
            return values_list
        object = {"key": current_node.key, "value": current_node.value}

        values_list.append(object)
        self.preorder_helper(current_node.left, values_list)
        self.preorder_helper(current_node.right, values_list)
        return values_list

    def preorder(self):
        values_list = []
        return self.preorder_helper(self.root, values_list)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def postorder_helper(self, current_node, values_list):
        if not current_node:
            return values_list
        object = {"key": current_node.key, "value": current_node.value}

        self.postorder_helper(current_node.left, values_list)
        self.postorder_helper(current_node.right, values_list)
        values_list.append(object)
        return values_list

    def postorder(self):
        values_list = []
        return self.postorder_helper(self.root, values_list)
        

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height_helper(self, current_node):
        if not current_node:
            return 0

        return max(self.height_helper(current_node.left), self.height_helper(current_node.right)) + 1
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