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
        if node == None:
            return

        # first add the data of node
        node_array.append({
            'key': node.key,
            'value': node.value
        })

        # then recur on left child
        self.preorder_helper(node.left, node_array)

        # lastly recur on right child
        self.preorder_helper(node.right, node_array)
        return node_array

    def preorder(self):
        # node, left, right
        node_array = []

        if self.root == None:
            return node_array

        return self.preorder_helper(self.root, node_array)

    # Time Complexity:
    # Space Complexity:
    def postorder_helper(self, node, node_array):
        # left,right,node
        if not node:
            return

        # first on left child
        self.postorder_helper(node.left, node_array)

        #  recur on right child
        self.postorder_helper(node.right, node_array)
        # then add the data of node
        node_array.append({
            'key': node.key,
            'value': node.value
        })


    def postorder(self):
        # node, left, right
        node_array = []

        if self.root == None:
            return node_array

        self.postorder_helper(self.root, node_array)
        return node_array


    # Time Complexity:
    # Space Complexity:
    def height_helper(self, node):
        if not node:
            return 0

        left = self.height_helper(node.left)
        right = self.height_helper(node.right)

        return max(left, right) + 1

    def height(self):
        if self.root == None:
            return 0

        return self.height_helper(self.root)

#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:
    def bfs(self):
        # store nodes
        result_arr = []

        if self.root is None:
            return result_arr

        #  start at root
        node_queue = []
        node_queue.append(self.root)

        # while we have something to process ...
        while len(node_queue) > 0:
            # pull off whats in node arr
            curr_node = node_queue.pop(0)

            if curr_node.left:
                node_queue.append(curr_node.left)
            if curr_node.right:
                node_queue.append(curr_node.right)
            result_arr.append({"key": curr_node.key, "value": curr_node.value})
        return result_arr


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
