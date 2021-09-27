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

    def add_helper(self, current_node, new_node):
        if current_node == None:
            return new_node

        if new_node.key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, new_node)
        else:
            current_node.right = self.add_helper(
                current_node.right, new_node)
        return current_node

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value=None):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            new_node = TreeNode(key, value)
            self.root = self.add_helper(self.root, new_node)

    def find_helper(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node.value
        if key < node.key:
            left_val = self.find_helper(node.left, key)
            return left_val
        else:
            right_val = self.find_helper(node.right, key)
            return right_val

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        return self.find_helper(self.root, key)

    def inorder_helper(self, node, res):
        if node == None:
            return
        self.inorder_helper(node.left, res)
        res.append({"key": node.key, "value": node.value})
        self.inorder_helper(node.right, res)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        res = []
        self.inorder_helper(self.root, res)
        return res

    def preorder_helper(self, node, res):
        if node == None:
            return
        res.append({"key": node.key, "value": node.value})
        self.preorder_helper(node.left, res)
        self.preorder_helper(node.right, res)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        res = []
        self.preorder_helper(self.root, res)
        return res

    def postorder_helper(self, node, res):
        if node == None:
            return
        self.postorder_helper(node.left, res)
        self.postorder_helper(node.right, res)
        res.append({"key": node.key, "value": node.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        res = []
        self.postorder_helper(self.root, res)
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def height(self):
        ans = 0
        queue = []
        if self.root == None:
            return ans

        queue.append(self.root)

        while queue:
            currSize = len(queue)
            while currSize > 0:
                currNode = queue.pop(0)
                currSize -= 1

                if currNode.left is not None:
                    queue.append(currNode.left)
                if currNode.right is not None:
                    queue.append(currNode.right)

            ans += 1
        return ans


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:


    def bfs(self):
        pass


#   # Useful for printing


    def to_s(self):
        return f"{self.inorder()}"
