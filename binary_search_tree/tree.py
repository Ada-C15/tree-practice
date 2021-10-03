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

    # Time Complexity:
    # Space Complexity:
    def add(self, key, value):
        current_node = self.root
        new_node = TreeNode(key, value)
        if current_node == None:
            self.root = new_node
        else:
            self.add_helper(current_node, key, value)

    def find_helper(self, current_node, key):
        if current_node == None:
            return None
        elif current_node.key == key:
            return current_node.value
        elif key <= current_node.key:
            return self.find_helper(current_node.left, key)
        else:
            return self.find_helper(current_node.right, key)

    # Time Complexity:
    # Space Complexity:

    def find(self, key):
        return self.find_helper(self.root, key)

    # Time Complexity:
    # Space Complexity:

    def inorder_helper(self, current_node, arr):
        if current_node:
            self.inorder_helper(current_node.left, arr)
            arr.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper(current_node.right, arr)
            # left_list = self.inorder_helper(current_node.left)
            # right_list = self.inorder_helper(current_node.right)
            # return left_list + [{"key": current_node.key, "value": current_node.value}] + right_list

    def inorder(self):
        current = self.root
        if not current:
            return []
        arr = []
        self.inorder_helper(current, arr)
        return arr

    # Time Complexity:
    # Space Complexity:

    def preorder_helper(self, current_node, arr):
        if current_node:
            arr.append({"key": current_node.key, "value": current_node.value})
            self.preorder_helper(current_node.left, arr)
            self.preorder_helper(current_node.right, arr)

    def preorder(self):
        current = self.root
        if not current:
            return []
        arr = []
        self.preorder_helper(current, arr)
        return arr

    def postorder_helper(self, current_node, arr):
        if current_node:
            self.postorder_helper(current_node.left, arr)
            self.postorder_helper(current_node.right, arr)
            arr.append({"key": current_node.key, "value": current_node.value})
    # Time Complexity:
    # Space Complexity:

    def postorder(self):
        current = self.root
        if not current:
            return []
        arr = []
        self.postorder_helper(current, arr)
        return arr

    def height_helper(self, current_node):
        if not current_node:
            return 0
        else:
            l_depth = self.height_helper(current_node.left)
            r_depth = self.height_helper(current_node.right)

            if l_depth > r_depth:
                return l_depth+1
            else:
                return r_depth+1

    # Time Complexity:
    # Space Complexity:
    def height(self):
        current_node = self.root
        return self.height_helper(current_node)


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:

    def bfs(self):
        pass


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"


empty_tree = Tree()

empty_tree.add(5, "Peter")
empty_tree.add(3, "Paul")
empty_tree.add(1, "Mary")
empty_tree.add(10, "Karla")
empty_tree.add(15, "Ada")
empty_tree.add(25, "Kari")

print(empty_tree.inorder())
