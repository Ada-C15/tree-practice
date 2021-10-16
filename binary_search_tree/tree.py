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

        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(
                current_node.right, key, value)
        return current_node

    # Time Complexity: O logn
    # Space Complexity: O n
    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: O log n
    # Space Complexity: O n
    def find(self, key):
        if self.root == None:
            return None

        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return None

    # Time Complexity:
    # Space Complexity:
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list

    # Time Complexity:
    # Space Complexity:

    def preorder_helper(self, current, traversal_list):
        if current != None:
            traversal_list.append({'key': current.key, 'value': current.value})
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, traversal_list):
        if current != None:
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append({'key': current.key, 'value': current.value})
    # Time Complexity: O Log n
    # Space Complexity: O n

    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    def height_help(self, current_node):
        if not current_node:
            return 0
        height_left = self.height_help(current_node.left)
        height_right = self.height_help(current_node.right)
        return max(height_left, height_right) + 1
    # Time Complexity: O log n
    # Space Complexity: O (1)

    def height(self):
        return self.height_help(self.root)


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:


    def bfs(self):
        pass


#   # Useful for printing


    def to_s(self):
        return f"{self.inorder()}"
