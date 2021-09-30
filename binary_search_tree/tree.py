class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key # if there's no incoming value, set it to the given key

        self.key = key
        self.value = val
        self.left = None # left pointer
        self.right = None # right pointer
        

class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key,value)
        else:
            parent = None
            current = self.root

            while current != None:
                parent = current
                if current.key > key:
                    current = current.left
                else:
                    current = current.right
            if parent.key > key:
                parent.left = TreeNode(key,value)
            else:
                parent.right = TreeNode(key,value)

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

    def inorder_helper(self, current_node, values):
        # base case
        if not current_node:
            return values

        self.inorder_helper(current_node.left, values)
        values.append({
            "key": current_node.key,
            "value": current_node.value
        })

        self.inorder_helper(current_node.right,values)
        return values
    
    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def inorder(self):
        values = []
        return self.inorder_helper(self.root, values)

    def preorder_helper(self, current_node, values):
        # base case
        if not current_node:
            return values

        values.append({
            "key": current_node.key,
            "value": current_node.value
        })

        self.preorder_helper(current_node.left,values)
        self.preorder_helper(current_node.right, values)
        return values

    # Time Complexity: O(logn n)
    # Space Complexity: O(n)  
    def preorder(self):
        values = []
        return self.preorder_helper(self.root, values)
    
    def postorder_helper(self, current_node, values):
        if not current_node:
            return values

        self.postorder_helper(current_node.left, values)
        self.postorder_helper(current_node.right, values)

        values.append({
            "key": current_node.key,
            "value":current_node.value
        })

        return values
    
    # Time Complexity: O(log n) 
    # Space Complexity: O(n)
    def postorder(self):
        values = []
        return self.postorder_helper(self.root, values)

    def height_helper(self, current_node):
        if not current_node:
            return 0
        left = self.height_helper(current_node.left)
        right = self.height_helper(current_node.right)

        return max(left, right) + 1
    
    # Time Complexity: O(log n)
    # Space Complexity: O(log n) >> ?     
    def height(self):
        return self.height_helper(self.root)


# completed for tests
    def bfs(self):
        final = []
        collection = []

        if self.root:
            collection.append(self.root)
        
        while len(collection) > 0:
            current_node = collection.pop(0)

            if current_node.left:
                collection.append(current_node.left)
            if current_node.right:
                collection.append(current_node.right)
            
            final.append({
                "key": current_node.key,
                "value": current_node.value
            })
        return final

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
