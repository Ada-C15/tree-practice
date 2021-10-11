class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    # marshalling is converting one datatype/format to another - this is to please the test - 
    # marshalling does not change the underlying data - just the format to make tests and various softwares happy
    def dict(self):
        return {"key": self.key, "value": self.value}
    
class Tree:
    def __init__(self):
        self.root = None


    def add_helper(self, current_node, new_node):
        if current_node == None:
            return new_node
        
        if new_node.key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, new_node)
        else:
            current_node.right = self.add_helper(current_node.right, new_node)

        return current_node
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    # recursive solution
    def add_recursive(self, key, value=None):
        node = TreeNode(key, value)
        if self.root == None:
            self.root = node
            return
        self.add_helper(self.root, node)

    # Time Complexity: O(log n) - if balanced
    # Space Complexity: O(1)
    # iterative solution

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

        if key <= previous.key:
            previous.left = node
        else:
            previous.right = node

    # Time Complexity: # binray search O(log n)
    # Space Complexity: O()
    # iterative solution (you don't need a helper function like in the recursive solution)
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

        # If you do not specify a return value - it will automatically return none in Python.
        # There is a return none automatically appended to the end of your funcitons
################### Find with Recursion ###############
        # Recursion is more eloquent - As long as you get the base case and the iterative case - 
        # the Recursions Fairy magically takes care of everything in the middle
    def find_helper(self, current, key):
        if current.key == key:
            return current.value
    
        if current.key > key:
            return self.find_helper(current.left, key)
        elif current.key < key:
            return self.find_helper(current.right, key)
        else:
            return None

    def find_recursive(self, key):
        if not self.root:
            return None
        return self.find_helper(self.root, key)
##################

##### inorder (left, root, right)
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
        # print(traversal_list)
        
        return traversal_list

###################### Need to do data transformation - MARSHALLING - Convert things to dictionaries #########
#### We have done a good job traversing the tree the way we are supposed to...
#### BUT we are returning the information in a format that the tests will not accept...
#### We must reformat the data to a list of dictionaries to pass the test...

##### preorder - APPEND First (root, left, right)  
    def preorder_helper(self, current, traversal_list):
        if current:
            
            traversal_list.append(current.dict()) # appending the current value to the traversal list before you append the parent's left-then-right nodes
            self.preorder_helper(current.left, traversal_list) # until the left is exhuasted
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity: 
    # Space Complexity:     
    # preorder gets used a lot to save things into a tree. 
    # We're going to generate a list of all the elements in the preorder traversal
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        print(traversal_list)
        
        return traversal_list

########################
# To Do List == call stack 
# How is the codeeeeee manage the stack - 
########################

##### postoder - APPEND LAST    (right, left, root)
    def postorder_helper(self, current, traversal_list):
        if current:
            self.postorder_helper(current.left, traversal_list)
            self.postordaer_helper(current.right, traversal_list)
            traversal_list.append(current.dict())

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        print(traversal_list)
        
        return traversal_list

    # Time Complexity: 
    # Space Complexity:     
    # Need a Full-Blown Traversal  - we can get the help of a reverse-recursion fairy

    def height_helper(self, current):
        if not current:
            return 0
        height_left = self.height_helper(current.left)
        height_right = self.height(current.right)
        return max(height_left, height_right) + 1
        
        # traverse the left
        # traverse right
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
