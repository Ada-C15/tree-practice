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


    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)     
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node


    # Time Complexity: O(log n) - balanced
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)


    def find_helper(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self.find_helper(current.left, key)
        else:
            return self.find_helper(current.right, key)


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def find(self, key):
        return self.find_helper(self.root, key)


    def inorder_helper(self, current, traversal_list):
        if current == None:
            return None
        self.inorder_helper(current.left, traversal_list)
        traversal_list.append({
                "key": current.key,
                "value": current.value
            })
        self.inorder_helper(current.right, traversal_list)


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list


    def preorder_helper(self, current, traversal_list):
        if current != None:
            traversal_list.append({
                "key": current.key,
                "value": current.value
            })
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)


    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list


    def postorder_helper(self, current, traversal_list):
        if current == None:
            return None
        self.postorder_helper(current.left, traversal_list)   
        self.postorder_helper(current.right, traversal_list)   
        traversal_list.append({
            "key": current.key,
            "value": current.value
        })


    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list


    def height_helper(self, current):
        if current == None:
            return 0
        else:
            left = self.height_helper(current.left)
            right = self.height_helper(current.right)
        return max(left,right) + 1


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height(self):
        current = self.root
        return self.height_helper(current)

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        
#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
