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



    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node
    
    
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value) 
        else:
            self.add_helper(self.root, key, value)


    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        
        current = self.root
        while current !=  None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left
            
        return None
        

    def inorder_helper(self, current, trav_list):
        if current == None:
            return 

        self.inorder_helper(current.left, trav_list)
        trav_list.append({"key":current.key, "value":current.value})
        self.inorder_helper(current.right, trav_list)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        trav_list = []
        self.inorder_helper(self.root, trav_list)
        return trav_list


    def preorder_helper(self, current, trav_list):
        if current == None:
            return 

        trav_list.append({"key":current.key, "value":current.value})
        self.preorder_helper(current.left, trav_list)
        self.preorder_helper(current.right, trav_list)

    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def preorder(self):
        trav_list = []
        self.preorder_helper(self.root, trav_list)
        return trav_list


    def postorder_helper(self, current, trav_list):
        if current == None:
            return

        self.postorder_helper(current.left, trav_list)
        self.postorder_helper(current.right, trav_list)
        trav_list.append({"key":current.key, "value": current.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def postorder(self):
        trav_list = []
        self.postorder_helper(self.root, trav_list)
        return trav_list


    def height_helper(self, current):
        if current == None:
            return 0

        left_height = self.height_helper(current.left)
        right_height = self.height_helper(current.right)

        if left_height > right_height:
            return left_height + 1
        return right_height + 1

    # Time Complexity: O(n)
    # Space Complexity: O(log n)    
    def height(self):
        return self.height_helper(self.root)
        


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        trav_list = []
        fringe = [self.root]

        while len(fringe) > 0:
            node = fringe.pop(0)
            if node == None:
                continue
            trav_list.append({"key":node.key, "value": node.value})
            fringe.append(node.left)
            fringe.append(node.right)
            
        return trav_list
        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
