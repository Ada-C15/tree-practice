class TreeNode:
    def __init__(self, key, val=None):
        if val is None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def to_json(self):
        return {
            "key": self.key,
            "value": self.value
        }


class Tree:
    def __init__(self):
        self.root = None

    # ----------- add ----------

    # Time Complexity: O(log n) for balanced BST, O(n) for unbalanced
    # Space Complexity: O(1)

    def add_helper(self, current, key, value):
        if current is None:
            return TreeNode(key, value)
        if current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        elif current.key < key:
            current.right = self.add_helper(current.right, key, value)
        return current

    def add(self, key, value=None):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # ----------- find ----------

    # Time Complexity: O(log n) for balanced BST, O(n) for unbalanced
    # Space Complexity: O(1)

    def find_helper(self, current, key):
        if current is None:
            return None
        if current.key == key:
            return current.value
        elif current.key >= key:
            return self.find_helper(current.left, key)
        elif current.key < key:
            return self.find_helper(current.right, key)

    def find(self, key):
        return self.find_helper(self.root, key)

    # ----------- in-order ----------

    # Time Complexity: O(n), because we visit each node once
    # Space Complexity: O(depth of the recursion) or O(h), where h is height
    # of the tree -> O(n) in the worst case

    def inorder_helper(self, current, result):
        if current:
            self.inorder_helper(current.left, result)
            result.append(current.to_json())
            self.inorder_helper(current.right, result)

    def inorder(self):
        if self.root is None:
            return list()

        result = list()
        self.inorder_helper(self.root, result)
        return result

# ----------- pre-order ----------

    # Time Complexity: ^
    # Space Complexity: ^

    def preorder_helper(self, current, result):
        if current:
            result.append(current.to_json())
            self.preorder_helper(current.left, result)
            self.preorder_helper(current.right, result)

    def preorder(self):
        if self.root is None:
            return list()

        result = list()
        self.preorder_helper(self.root, result)
        return result

# ----------- post-order ----------
    # Time Complexity: ^
    # Space Complexity: ^

    def postorder_helper(self, current, result):
        if current:
            self.postorder_helper(current.left, result)
            self.postorder_helper(current.right, result)
            result.append(current.to_json())

    def postorder(self):
        if self.root is None:
            return list()

        result = list()
        self.postorder_helper(self.root, result)
        return result

# ----------- height ----------

    # Time Complexity: O(log n) for balanced, O(n)  for unbalanced
    # Space Complexity: O(n)

    def height_helper(self, current):
        if current is None:
            return 0
        else:
            return 1 + max(self.height_helper(current.left),
                           self.height_helper(current.right))

    def height(self):
        if self.root is None:
            return 0
        else:
            return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:

    def bfs(self):
        pass


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"
