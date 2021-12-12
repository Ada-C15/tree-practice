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

    # Time Complexity: if tree is balanced, O(log n), if unbalanced, O(n)
    # Space Complexity: O(long n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        if key <= current_node.key:
            current_node.left = self.add_helper(
                current_node.left, key, value)
        else: 
            current_node.right = self.add_helper(
                current_node.right, key, value)
        return current_node

    # Time Complexity: O(log n)
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
    def inorder(self):
        result = []
        if self.root == None:
            return result
        return self.inorder_helper(self.root, result)
    
    def inorder_helper(self, root, result):
        if root:
            self.inorder_helper(root.left, result)
            result.append({'key': root.key, 'value': root.value})
            self.inorder_helper(root.right, result)
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def preorder(self):
        result = []
        if self.root == None:
            return result
        return self.preorder_helper(self.root, result)
    
    def preorder_helper(self, root, result):
        if root:
            result.append({'key': root.key, 'value': root.value})
            self.preorder_helper(root.left, result)
            self.preorder_helper(root.right, result)
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        result = []
        if self.root == None:
            return result
        return self.postorder_helper(self.root, result)

    def postorder_helper(self, root, result):
        if root:
            self.postorder_helper(root.left, result)
            self.postorder_helper(root.right, result)
            result.append({'key': root.key, 'value': root.value})
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):
        if self.root == None:
            return 0
        return self.height_helper(self.root)
    
    def height_helper(self, root):
        if root == None:
            return 0
        
        left_height = self.height_helper(root.left)
        right_height = self.height_helper(root.right)
        tree_height = max(left_height, right_height) + 1
        return tree_height

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
