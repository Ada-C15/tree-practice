class TreeNode:
    def __init__(self, key, val=None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def height(self):
        if self.right and self.left:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 1


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log N)
    # Space Complexity: O(1)

    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(
                current_node.right, key, value)
        return current_node

    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
            # parent = None
            # current = self.root
            # while current != None:
            #     parent = current
            #     if current.key >= key:
            #         current = current.left
            #     else:
            #         current = current.right

            # if parent.key > key:
            #     parent.left = TreeNode(key, value)
            # else:
            #     parent.right = TreeNode(key, value)

    # Time Complexity: O(log N)
    # Space Complexity: O(1)
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

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder_helper(self, current, traversal_list):
        if not current:
            return traversal_list

        obj = {'key': current.key, 'value': current.value}
        self.inorder_helper(current.left, traversal_list)
        traversal_list.append(obj)
        self.inorder_helper(current.right, traversal_list)
        return traversal_list

    def inorder(self):
        traversal_list = []
        return self.inorder_helper(self.root, traversal_list)

    # Time Complexity: O(n)
    # Space Complexity:O(n)
    def preorder_helper(self, current, traversal_list):
        if current:
            obj = {'key': current.key, 'value': current.value}
            traversal_list.append(obj)
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)

        return traversal_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        pass

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height(self):
        if self.root:
            return self.root.height()
        else:
            return 0


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:

    def bfs(self):
        pass


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"
