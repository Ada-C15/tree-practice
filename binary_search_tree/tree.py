# from _typeshed import Self
from typing import Counter


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

    # Time Complexity:
    # Space Complexity:
    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        if current_node.key > key:
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

    # Time Complexity:
    # Space Complexity:
    def find_helper(self, current_node, key):
        if current_node == None:
            return None
        elif current_node.key == key:
            return current_node.value
        elif key < current_node.key:
            return self.find_helper(current_node.left, key)
        return self.find_helper(current_node.right, key)

    def find(self, key):
        # enter recursion
        return self.find_helper(self.root, key)

    # Time Complexity:
    # Space Complexity:

    def inorder_helper(self, node, node_array):
        if node == None:
            return
        # First recur on left child
        self.inorder_helper(node.left, node_array)
        # then add the data of node
        node_array.append({
            'key': node.key,
            'value': node.value
        })
        # now recur on right child
        self.inorder_helper(node.right, node_array)
        return node_array

    def inorder(self):
        node_array = []

        if self.root == None:
            return node_array
        return self.inorder_helper(self.root, node_array)

    # Time Complexity:
    # Space Complexity:

    def preorder_helper(self, node, node_array):
        if not node:
            return

        # node,left,right
        # first add the data of node
        node_array.append({
            'key': node.key,
            'value': node.value
        })

        # then recur on left child
        self.inorder_helper(node.left, node_array)

        # lastly recur on right child
        self.inorder_helper(node.right, node_array)
        
        return node_array

    def preorder(self):
        # node, left, right
        node_array = []

        if self.root == None:
            return node_array
        
        return self.preorder_helper(self.root, node_array)

    # Time Complexity:
    # Space Complexity:
    def postorder(self):
        pass

    # Time Complexity:
    # Space Complexity:
    def height(self):
        pass


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:

    def bfs(self):
        pass


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"
