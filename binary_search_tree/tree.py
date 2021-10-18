# some descriptive blocks and None's are for readability

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

    # Time Complexity: if balanced, O(log n); else: O(n)
    # Space Complexity: O(1)
    def add(self, key, value=None):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            current = self.root
            while True:
                if key > current.key:
                    if current.right is None:
                        current.right = TreeNode(key, value)
                        return
                    current = current.right
                else:
                    if current.left is None:
                        current.left = TreeNode(key, value)
                        return
                    current = current.left

# ---------------------------------------------------------------

    # Time Complexity: if balanced, O(log n); else: O(n)
    # Space Complexity: O(1)
    def find(self, key):
        return self.find_recursive(key, self.root)

    def find_recursive(self, key, current_node):
        if current_node is None:
            return None
        if key == current_node.key:
            return current_node.value
        if key > current_node.key:
            return self.find_recursive(key, current_node.right)
        else:
            return self.find_recursive(key, current_node.left)

# ---------------------------------------------------------------

    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def inorder(self):
        node_list = []
        self.inorder_recursive(self.root, node_list)
        return node_list

    def inorder_recursive(self, node, node_list):
        if node is None:
            return
        self.inorder_recursive(node.left, node_list)
        node_list.append(self.to_dic(node))
        self.inorder_recursive(node.right, node_list)

# ---------------------------------------------------------------

    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def preorder(self):
        node_list = []
        self.preorder_recursive(self.root, node_list)
        return node_list

    def preorder_recursive(self, node, node_list):
        if node is None:
            return
        node_list.append(self.to_dic(node))
        self.preorder_recursive(node.left, node_list)
        self.preorder_recursive(node.right, node_list)

# ---------------------------------------------------------------

    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def postorder(self):
        node_list = []
        self.postorder_recursive(self.root, node_list)
        return node_list

    def postorder_recursive(self, node, node_list):
        if node is None:
            return
        self.postorder_recursive(node.left, node_list)
        self.postorder_recursive(node.right, node_list)
        node_list.append(self.to_dic(node))

# ---------------------------------------------------------------

    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def height(self):
        return self.height_recursive(self.root)

    def height_recursive(self, node):
        if node is None:
            return 0
        return max(self.height_recursive(node.left), self.height_recursive(node.right)) + 1
        # ..🌝

# ---------------------------------------------------------------

#   # Optional Method
#   # Time Complexity:  O(n)
#   # Space Complexity: O(n)

    def bfs(self):
        result = []
        if self.root is None:
            return result

        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop(0)
            result.append(self.to_dic(current))
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print(result)
        return result

# ---------------------------------------------------------------

#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"

    def to_dic(self, node):
        return {"key": node.key, "value": node.value}
