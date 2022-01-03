class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
    
    def dict(self):
        return {"key": self.key, "value": self.value}
        


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        tree = TreeNode(key, value)

        if self.root == None:
            self.root = tree
        else:
            current = self.root
            
            while current != None:
                if key == current.key:
                    return None
                if key < current.key:
                    if current.left == None:
                        current.left = tree
                    current = current.left
                elif key > current.key:
                    if current.right == None:
                        current.right = tree
                    current = current.right

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        current = self.root
        while current != None:
            if key == current.key:
                return current.value
            elif key > current.key:
                current = current.right
            else:
                current = current.left 
        return None

    def inorder_helper(self, current, traversal_list):
        if current == None:
            return

        self.inorder_helper(current.left, traversal_list)
        traversal_list.append(current.dict())
        self.inorder_helper(current.right, traversal_list)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list   

    def preorder_helper(self, current, traversal_list):
        if current == None:
            return

        traversal_list.append(current.dict())
        self.preorder_helper(current.left, traversal_list)
        self.preorder_helper(current.right, traversal_list)

    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, traversal_list):
        if current == None:
            return

        self.postorder_helper(current.left, traversal_list)
        self.postorder_helper(current.right, traversal_list)
        traversal_list.append(current.dict())

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    def height_helper(self, current):
        if current == None:
            return 0
        left_height = self.height_helper(current.left)
        right_height = self.height_helper(current.right)
        return 1 +max(left_height, right_height)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass
#  Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
