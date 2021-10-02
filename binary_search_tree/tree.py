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

    def add_helper(self, current_node, new_node):
        if current_node == None:
            return new_node

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        node = TreeNode(key, value)
        if self.root == None:
            self.root = node
            return

        previous = None
        current = self.root
        while current != None:
            previous = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if key < previous.key:
            previous.left = node
        else:
            previous.right = node
                

    # Time Complexity: 
    # Space Complexity: 
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


    def find_helper(self, current, key):
        if current.key == key:
            return current.value
        if current.key > key:
            return self.find_helper(current.left, key)
        else:
            return None

    def find_recursive(self, key):
        if not self.root:
            return None
        return self.find_helper(self.root, key)


    def inorder_helper(self, current, traversal_list):
        if current:
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append(current.dict())
            self.inorder_helper(current.right, traversal_list)


    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list


    def preorder_helper(self, current, traversal_list):
        if current:

            traversal_list.append(current.dict()) #append the current value to the traversal list before going to the left
            self.preorder_helper(current.left, traversal_list) # until the left cannot go left anymore
            self.preorder_helper(current.right, traversal_list)


    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        print(traversal_list)
        return traversal_list


    def postorder_helper(self, current, traversal_list):
        if current:
            self.postorder_helper(current.left, traversal_list) 
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append(current.dict())
            return

    # Time Complexity: 
    # Space Complexity:   
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        print(traversal_list)

        return traversal_list

    # Time Complexity: 
    # Space Complexity:
    def height_helper(self, current):
        if not current:
            return 0
        height_left = self.height_helper(current.left)
        height_right = self.height_helper(current.right)
        return max(height_left, height_right) + 1
    
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
