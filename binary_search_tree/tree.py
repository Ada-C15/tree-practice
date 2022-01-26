class TreeNode:
    def __init__(self, key, val=None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def add(self, key, value=None):
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key, value)
                return self.left
            return self.left.add(key, value)
        else:
            if self.right is None:
                self.right = TreeNode(key, value)
                return self.right
            return self.right.add(key, value)

    def inorder(self, list):
        if self.left is not None:
            self.left.inorder(list)

        list.append({
            "key": self.key,
            "value": self.value
        })

        if self.right is not None:
            self.right.inorder(list)

    def preorder(self, list):
        list.append({
            "key": self.key,
            "value": self.value
        })

        if self.left is not None:
            self.left.preorder(list)

        if self.right is not None:
            self.right.preorder(list)

    def postorder(self, list):
        if self.left is not None:
            self.left.postorder(list)

        if self.right is not None:
            self.right.postorder(list)

        list.append({
            "key": self.key,
            "value": self.value
        })

    def height(self):
        if self.left is None:
            leftHeight = 0
        else:
            leftHeight = self.left.height()

        if self.right is None:
            rightHeight = 0
        else:
            rightHeight = self.right.height()

        return 1 + max(leftHeight, rightHeight)


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity:
    # Space Complexity:
    def add(self, key, value=None):
        if self.root is None:
            self.root = TreeNode(key, value)
            return self.root
        else:
            return self.root.add(key, value)

    def find_helper(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self.find_helper(current.left, key)

        return self.find_helper(current.right, key)

    # Time Complexity: o(1)
    # Space Complexity:o(n)
    def find(self, key):
        return self.find_helper(self.root, key)

    # Time Complexity:  o(1)
    # Space Complexity: o(1)
    def inorder(self):
        list = []
        if self.root is not None:
            self.root.inorder(list)
        return list

    # Time Complexity: o(n)
    # Space Complexity:0(n)

    def preorder(self):
        list = []
        if self.root is not None:
            self.root.preorder(list)
        return list

    # Time Complexity: 0(log n)
    # Space Complexity:o(1)
    def postorder(self):
        list = []
        if self.root is not None:
            self.root.postorder(list)
        return list

    # Time Complexity: o(n)
    # Space Complexity:0(n)
    def height(self):
        if self.root is None:
            return 0
        return self.root.height()


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:

    def bfs(self):
        pass


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"
