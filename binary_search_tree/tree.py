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
        elif key <= current_node:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(
                current_node.right, key, value)

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
            elif key < current.key:  # if there is a left node keep searching
                current = current.left
            else:
                current = current.right
        return None

    def inorder_helper(self, root, elements):
        if root == None:
            return

        # if there is left, traverse
        self.inorder_helper(root.left, elements)
        # append the last left node that becomes the "root"
        elements.append({"key": root.key, "value": root.value})
        # if there is right, traverse (it will start from left recursive)
        self.inorder_helper(root.right, elements)
        return

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        # order: left, root, right
        # if there are no nodes, return empty list
        if self.root == None:
            return []

        elements = []
        self.inorder_helper(self.root, elements)

        return elements

    def preorder_helper(self, root, elements):
        if root == None:
            return

        # if there is root, add that
        elements.append({"key": root.key, "value": root.value})
        # if there is a left, traverse that
        self.preorder_helper(root.left, elements)
        # then traverse right
        self.preorder_helper(root.right, elements)
        return

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        # order: root, left, right
        if self.root == None:
            return []

        elements = []
        self.preorder_helper(self.root, elements)

    def postorder_helper(self, root, elements):
        if root == None:
            return

        self.postorder_helper(root.left, elements)
        self.postorder_helper(root.right, elements)
        elements.append({"key": root.key, "value": root.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        # order: left, right, current
        if self.root == None:
            return []

        elements = []
        self.postorder_helper(self.root, elements)

    def max_height_helper(self, root, height):
        if root == None:
            return height

        # else return +1 of left and right subtress
        left_height = 1 + self.max_height_helper(root.left, height)
        right_height = 1 + self.max_height_helper(root.right, height)

        # compare to find max
        if left_height < right_height:
            return right_height
        else:
            return left_height

    # Time Complexity: O(n)
    # Space Complexity: O(log n)
    def height(self):
        if self.root:
            return self.max_height_helper(self.root, 0)
        return 0

#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:
    def bfs(self):
        pass


#   # Useful for printing


    def to_s(self):
        return f"{self.inorder()}"
