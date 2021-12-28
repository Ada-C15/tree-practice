class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
# we need to sort the values by key, or else v and k will remain the same.
class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        n_node = TreeNode(key, value)
        if not self.root:
            self.root = n_node
            return None
        current = self.root

        while True:
            if current.key > key and current.left is None:
                current.left = n_node
                return None
            elif current.key <= key and current.right is None:
                current.right = n_node
                return None
            elif current.key > key:
                current = current.left
            else:
                current = current.left


    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif current.key > key:
                current = current.left
            else: current = current.right
        return None


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        trees = []
        return self.awesome_helper_inorder(self.root, trees)

    def awesome_helper_inorder(self, current, trees):
        if not current:
            return trees
        curr_storage = {"key": current.key, "value": current.value}

        self.awesome_helper_inorder(current.left, trees)
        trees.append(curr_storage)
        self.awesome_helper_inorder(current.right, trees)

        return trees

    # Time Complexity: O(n)
    # Space Complexity:O(n)     
    def preorder(self):
        if not self.root:
            return []
        left = Tree()
        left.root = self.root.left
        right = Tree()
        right.root = self.root.right

        return [{"key": self.root.key, "value": self.root.value}] + left.preorder() + right.preorder()

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        if not self.root:
            return []

        left = Tree()
        left.root = self.root.left
        right = Tree()
        right.root = self.root.right

        return left.postorder() + right.postorder() + [{"key": self.root.key, "value": self.root.value}]

    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def height(self):
        if not self.root:
            return 0
        left = Tree()
        left.root = self.root.left
        right = Tree()
        right.root = self.root.right

        return max(left.heigh(),right.height()) +1


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
