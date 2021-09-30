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

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if self.root == None:
            self.root = new_node
            return

        previous = None
        current = self.root
        while current != None:
            previous = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right

        if key <= previous.key:
            previous.left = new_node
        else:
            previous.right = new_node

    # Time Complexity: O(log n)
    # Space Complexity: 
    def find(self, key):
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return None

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        pass

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
