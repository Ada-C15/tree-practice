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

    # def add_helper(self, current, key, value=None):
    #     if current == None:
    #         return TreeNode(key, value)
    #     if key <= current.key:
    #         current.left = self.add_helper(current.left, key, value)
    #     else:
    #         current.right = self.add_helper(current.right, key, value)
    #     return current

    # # Time Complexity:
    # # Space Complexity:
    # def add(self, key, value=None):
    #     if self.root == None:
    #         self.root = TreeNode(key, value)
    #     self.add_helper(self.root, key, value)

    def add_helper(self, current_node, new_node):
        if current_node == None:
            return new_node

        if new_node.key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, new_node)
        else:
            current_node.right = self.add_helper(current_node.right, new_node)

        return current_node

    # # Time Complexity: O(log n)
    # # Space Complexity: O(1)
    def add(self, key, value=None):
        node = TreeNode(key, value)
        if self.root == None:
            self.root = node
            return

        self.add_helper(self.root, node)

    def find_helper(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self.find_helper(current.left, key)

        return self.find_helper(current.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        return self.find_helper(self.root, key)

    def inorder_helper(self, current, traversal_list):
        if current != None:
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append({'key': current.key, 'value': current.value})
            self.inorder_helper(current.right, traversal_list)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list

    def preorder_helper(self, current, traversal_list):
        if current != None:
            traversal_list.append({'key': current.key, 'value': current.value})
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, traversal_list):
        if current != None:
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append({'key': current.key, 'value': current.value})

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    def height_helper(self, current):
        if current == None:
            return 0
        left = self.height_helper(current.left)
        right = self.height_helper(current.right)

        return max(left, right) + 1

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def height(self):
        return self.height_helper(self.root)
        # if current node is None, return 0
        # if self.root == None:
        #     return 0
        # else:
        #     # otherwise, return the max height of the right and left subtrees + 1
        #     left_height = self.height(self.root.left)
        #     right_height = self.height(self.root.right)

        #     if left_height >= right_height:
        #         return left_height + 1
        #     else:
        #         return right_height + 1



#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
