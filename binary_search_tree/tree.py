

class TreeNode:
    def __init__(self, key, value = None):
        if value == None:
            value = key

        self.key = key
        self.value = value
        self.left = None
        self.right = None
        


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
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def inorder(self):
        tree_nodes = []

        if self.root == None:
            return tree_nodes
        else:
            return self.inorder_helper(self.root, tree_nodes)

    def inorder_helper(self, current, tree_nodes):
        if current == None:
            return None

        self.inorder_helper(current.left, tree_nodes)
        
        tree_nodes.append(
                {
                    "key": current.key, 
                    "value": current.value
                }
            )

        self.inorder_helper(current.right, tree_nodes)

        return tree_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(1)     
    def preorder(self):
        tree_nodes = []

        if self.root == None: 
            return tree_nodes 
        else:
            return self.preorder_helper(self.root, tree_nodes)

    def preorder_helper(self, current, tree_nodes):
        if current == None: 
            return None 

        tree_nodes.append(
            {
                "key": current.key,
                "value": current.value
            }
        )

        self.preorder_helper(current.left, tree_nodes)

        self.preorder_helper(current.right, tree_nodes)

        return tree_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(1)     
    def postorder(self):
        tree_nodes = []


        return self.postorder_helper(self.root, tree_nodes)
    
    def postorder_helper(self, current, tree_nodes):
        if current == None:
            return tree_nodes

        self.postorder_helper(current.left, tree_nodes)

        self.postorder_helper(current.right, tree_nodes)

        tree_nodes.append(
            {
                "key": current.key,
                "value": current.value
            }
        )

        return tree_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):

        return self.height_helper(self.root)

    def height_helper(self, current):
        if current == None:
            return 0

        left_height = self.height_helper(current.left)
        
        right_height = self.height_helper(current.right)

        return max(left_height, right_height) + 1

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
