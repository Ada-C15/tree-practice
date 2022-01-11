class TreeNode:
    def __init__(self, key, value=None):
        if value == None:
            value = key

        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log(n))*assumes all balanced tree
    # Space Complexity: O(1)
    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        if key < current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def find(self, value):
        return self.find_helper(self.root, value)

    def find_helper(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self.find_helper(current.left, key)
        return self.find_helper(current.right, key)

    # Time Complexity: O(logn)
    # Space Complexity: O(n)
    def inorder(self):
        array = []
        if self.root == None:
            return array
        return self.inorder_helper(self.root, array)

    def inorder_helper(self, current, array):
        if current == None:
            return
        self.inorder_helper(current.left, array)
        array.append({"key": current.key, "value": current.value})
        self.inorder_helper(current.right, array)
        return array

    # Time Complexity: O(logn)
    # Space Complexity: O(n)
    def preorder(self):
        array = []
        if self.root == None:
            return array
        return self.preorder_helper(self.root, array)

    def preorder_helper(self, current, array):
        if current == None:
            return
        array.append({"key": current.key, "value": current.value})
        self.preorder_helper(current.left, array)
        self.preorder_helper(current.right, array)
        return array

    # Time Complexity: O(logn)
    # Space Complexity: O(n)
    def postorder(self):
        array = []
        if self.root == None:
            return array
        return self.postorder_helper(self.root, array)

    def postorder_helper(self, current, array):
        if current == None:
            return
        self.postorder_helper(current.left, array)
        self.postorder_helper(current.right, array)
        array.append({"key": current.key, "value": current.value})
        return array

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def height(self):
        if self.root == None:
            return 0
        return self.height_helper(self.root)

    def height_helper(self, current):
        if current == None:
            return 0
        left = self.height_helper(current.left)
        right = self.height_helper(current.right)
        return max(left, right) + 1

    #   # Optional Method
    #   # Time Complexity:
    #   # Space Complexity:
    def bfs(self):
        pass

    #   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
