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

    def inorder_helper(self, current, traversal_list):
        if current:
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append(
                {
                    "key": current.key,
                    "value": current.value
                }
            )
            self.inorder_helper(current.right, traversal_list)

    # Time Complexity: O(recursion craziness)
    # Space Complexity:
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        print(traversal_list)
        return traversal_list

    def preorder_helper(self, current, traversal_list):
        if current:
            traversal_list.append(
                {
                    "key": current.key,
                    "value": current.value
                }
            )
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)
    
    # Time Complexity: O(terrible)
    # Space Complexity:     
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, traversal_list):
        if current:
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append(
                {
                    "key": current.key,
                    "value": current.value
                }
            )
    # Time Complexity: O(recursion)
    # Space Complexity:
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

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
