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

    # Time Complexity: O(log n)
    # Space Complexity: O(log n )

    def add_helper(self, current, key, value):
        if current is None:
            return TreeNode(key, value)
        if current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        else:
            current.right = self.add_helper(current.right, key, value)
        return current

    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)


    # Time Complexity: O( log n )
    # Space Complexity: O (log 1 )
    def find(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif current.key > key:
                current = current.left
            else:
                current = current.right

    # Time Complexity: O( n )
    # Space Complexity: O( n )
    def inorder_helper(self, current_node, listofvalues):
        if not current_node:
            return listofvalues
        obj = {'key': current_node.key, 'value': current_node.value}
        listofvalues.append(obj)
        self.inorder_helper(current_node.right, listofvalues)

    def inorder(self):
        listofvalues = []
        return self.inorder_helper(self.root, listofvalues)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder_helper(self, current_node, listofvalues):
        if not current_node:
            return listofvalues
        obj = {'key': current_node.key, 'value': current_node.value}
        listofvalues.append(obj)
        self.preorder_helper(current_node.left, listofvalues)
        self.preorder_helper(current_node.right, listofvalues)
        return listofvalues

    def preorder(self):
        listofvalues = []
        return self.preorder_helper(self.root, listofvalues)
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def postorder_helper(self, current_node, listofvalues):
        if not current_node:
            return listofvalues
        obj = {'key': current_node.key, 'value':current_node.value}
        self.postorder_helper(current_node.left, listofvalues)
        self.postorder_helper(current_node.right, listofvalues)
        listofvalues.append(obj)

    def postorder(self):
        listofvalues = []
        return self.postorder_helper(self.root, listofvalues)
    # Time Complexity: O(n)
    # Space Complexity: O(log n)    
    def height_helper(self, current_node):
        if not current_node:
            return 0
        return max(self.height_helper(current_node.left), self.height_helper(current_node.right)) + 1

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
