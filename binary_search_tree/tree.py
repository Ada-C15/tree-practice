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


    # Time Complexity: O(log n) if balanced
    # Space Complexity: 
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
            # parent = None
            # current = self.root
            # while current != None:
            #     parent = current
            #     if current.key > key:
            #         current = current.left
            #     else:
            #         current = current.right
            # if parent.key > key:
            #     parent.left = TreeNode(key, value)
            # else:
            #     parent.right = TreeNode(key, value)   
    
    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value) 
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node


    # Time Complexity: O(log n) if balanced 
    # Space Complexity: 
    def find(self, key):
        return self.find_helper(self.root, key)

    def find_helper(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self.find_helper(current.left, key)
        return self.find_helper(current.right, key)


    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list

    def inorder_helper(self, current, traversal_list):
        if current != None:
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append(current.dict())
            self.inorder_helper(current.right, traversal_list)


    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list
    
    def preorder_helper(self, current, traversal_list):
        if current != None:
            traversal_list.append(current.dict())
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)


    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list
    
    def postorder_helper(self, current, traversal_list):
        if current != None:
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append(current.dict())


    # Time Complexity: O(n)
    # Space Complexity: O(n)     
    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, current):
        if current == None:
            return 0
        left_subtree_height = self.height_helper(current.left)
        right_subtree_height = self.height_helper(current.right)
        return max(left_subtree_height, right_subtree_height) + 1


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"


# REMOVE LATER
# for testing purposes ... 
tree = Tree()
print(tree.root == None)
tree.add(5, "Piper")
tree.add(7, "Bowen")
tree.add(10)
tree.add(3)
tree.add(4)

print(tree.root.key == 5)
print(tree.root.right.key == 7)
print(tree.root.right.right.key == 10)
print(tree.root.left.key == 3)
print(tree.root.left.right.key == 4)

print(tree.find(5) == "Piper")
print(tree.find(7) == "Bowen")
print(tree.find(4) == 4)

tree.preorder()
tree.postorder()