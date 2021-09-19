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

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
            return None

        curr = self.root

        while True:
            if curr.key > key and curr.left is None:
                curr.left = new_node
                return None
            elif curr.key <= key and curr.right is None:
                curr.right = new_node
                return None
            elif curr.key > key:
                curr = curr.left
            
            else:
                curr = curr.right

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def find(self, key):
        curr = self.root

        while curr:
            if curr.key == key:
                return curr.value
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right
        return None 
        

    # Time Complexity: O(n) with n being the number of nodes
    # Space Complexity: O(n)
    def inorder(self):
        if not self.root:
            return []

        left_tree = Tree()
        left_tree.root = self.root.left
        right_tree = Tree()
        right_tree.root = self.root.right

        return left_tree.inorder() + [{"key": self.root.key, "value": self.root.value}] + right_tree.inorder()
        

    # Time Complexity: O(n) with n being the number of nodes
    # Space Complexity: O(n)   
    def preorder(self):
        if not self.root:
            return []

        left_tree = Tree()
        left_tree.root = self.root.left
        right_tree = Tree()
        right_tree.root = self.root.right

        return [{"key": self.root.key, "value": self.root.value}] + left_tree.preorder() + right_tree.preorder()

    # Time Complexity: O(n) with n being the number of nodes
    # Space Complexity: O(n)    
    def postorder(self):
        if not self.root:
            return []

        left_tree = Tree()
        left_tree.root = self.root.left
        right_tree = Tree()
        right_tree.root = self.root.right

        return left_tree.postorder() + right_tree.postorder() + [{"key": self.root.key, "value": self.root.value}]

    # Time Complexity: O(n) with n being the number of nodes
    # Space Complexity: O(n)      
    def height(self):
        if not self.root:
            return 0

        left_tree = Tree()
        left_tree.root = self.root.left
        right_tree = Tree()
        right_tree.root = self.root.right

        return max(left_tree.height() , right_tree.height()) + 1


#   # Optional Method
    # Time Complexity: O(n) with n being the number of nodes
    # Space Complexity: O(n) 
    def bfs(self):
        bfs_array = []
        if not self.root:
            return []
        curr_level = [self.root]
        while curr_level:
            bfs_array += [{"key": node.key, "value": node.value} for node in curr_level]
            curr_level = self.get_next_level(curr_level)
        return bfs_array

    def get_next_level(self, curr_level):
        next_level = []
        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        return next_level

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
