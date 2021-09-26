class TreeNode:
    def __init__(self, key, val = None):

        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def dict(self):
        return {'key': self.key, 'value': self.value}
        
class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n) - IF BALANCE - because you are not traveling through all nodes but instead, check if > than or smaller so you cut through half every time?
    # Space Complexity: O(1)  building one new node only no matter how big tree is, it only increases by 1 
    def add(self, key, value = None):
        # no root, no binary tree, first node added
        if not self.root:
            self.root = TreeNode(key, value)
            return
        # initializing parent outside loop
        parent = None 
        current = self.root
        # need to move it to the left or right to check
        while current:
            # parent move node by node to check every time loop runs
            parent = current
            if key > current.key:
                current = current.right
            # if they are same value, still going left
            else:  #  key <= current.key
                current = current.left
        
        if key <= parent.key:
            # add it to left node of parent
            parent.left = TreeNode(key, value)
        else:
            # add it to left node of parent
            parent.right = TreeNode(key, value)

    def add_helper(self, current_node, key, value):
        # base case - we are at the begining (root) 
        # or at the end (leaf)  so -> we add a new node 
        if not current_node:
            # can create it there
            return TreeNode(key, value)
        # there is a current node so we need to compare with it
        if key <= current_node.key:
        # going to add it in the left node because is smaller
        # first - we check (recursively) until it finds a leaf where it's smaller than current_node
            current_node.left = self.add_helper(current_node.left, key, value)
        else: # or a leaf to the right -  if number is greater than current_node
            current_node.right = self.add_helper(current_node.right, key, value)
        # we are at the end  here - the parent of this node's left or right is going to be set to this
        return current_node

    # Time Complexity: O(log n) - if balanced
    # Space Complexity: O(log n) - you are putting things on the stack for each level loked at
    def add_recursively(self, key, value = None):
        # no root, no binary tree, first node added
        if not self.root:
            self.root = TreeNode(key, value)
            return
        # use helper to recursively check til we find a leaf?
        self.add_helper(self.root, key, value)

    # Time Complexity: O(log n) - if balanced
    # Space Complexity: O(1) = not creating new data but reusing same variable?
    def find(self, key):
        # no root, no binary tree, not found
        if not self.root:
            return None

        current = self.root
        # 3 cases:
        while current:
        # 1 in current node
            if key == current.key:
                return current.value
        # 2 smaller than current
            elif key < current.key:
                current = current.left
        # 3 greater than current
            else: # key > current
                current = current.right
        # value is not in the tree
        return None
        
    # Time Complexity: 
    # Space Complexity: 
    def inorder_help(self, current_node, traversal_list):
        if current_node:

            self.inorder_help(current_node.left, traversal_list)
            traversal_list.append(current_node.dict())
            self.inorder_help(current_node.right, traversal_list)

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        traversal_list = []
        self.inorder_help(self.root, traversal_list)
        return traversal_list

    # Time Complexity: 
    # Space Complexity:
    def preorder_help(self, current_node, traversal_list):
        if current_node:
            traversal_list.append(current_node.dict())
            self.preorder_help(current_node.left, traversal_list)
            self.preorder_help(current_node.right, traversal_list)
        
    # Time Complexity: 
    # Space Complexity:
    def preorder(self):
        traversal_list = []
        self.preorder_help(self.root, traversal_list)
        return traversal_list

    def postorder_help(self, current_node, traversal_list):
        if current_node:
            self.postorder_help(current_node.left, traversal_list)
            self.postorder_help(current_node.right, traversal_list)
            traversal_list.append(current_node.dict())

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        traversal_list = []
        self.postorder_help(self.root, traversal_list)
        return traversal_list

    def height_help(self, current_node):
        if not current_node:
            return 0
        height_left = self.height_help(current_node.left)
        height_right = self.height_help(current_node.right)
        return max(height_left, height_right) + 1
    
    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        return self.height_help(self.root)

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
