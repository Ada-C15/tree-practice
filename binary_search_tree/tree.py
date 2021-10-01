class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    # marshalling is converting on datatype/format to another 
    # marshalling does not change the underlying data - just the format to make tests and various softwares
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

    # if you do not specify a return value - it will automatically return none in python
    # there is a return none automatically appeneded to the end of your functions
    # find with recursion as it is more eloquent - as long as you get the base case and the iterative case
    # recurion takes care of everything in the middle

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

    # inorder (left, root, right) Append in the middle
    # inorder is printing in the middle of the traversal

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


    # Need to do data transformation - Marshalling - convert things to dictionaries
    #We must reformat the data to a list of dictionaries to pass the test
    ## preorder (root, left, right) Append first

    def preorder_helper(self, current, traversal_list):
        if current:

            traversal_list.append(current.dict()) #append the current value to the traversal list before going to the left
            self.preorder_helper(current.left, traversal_list) # until the left cannot go left anymore
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity: 
    # Space Complexity:    
    # preorder gets used a lot to save things into a tree
    # preorder is printing before you do the traversal
    # We are going to generate a list of all the elements in the preorder traversal 

    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        print(traversal_list)
        return traversal_list

    # To do list == call stack
    # How does the code manage the stack - 

    def postorder_helper(self, current, traversal_list):
        if current:
            self.postorder_helper(current.left, traversal_list) 
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append(current.dict())
            return

    # Time Complexity: 
    # Space Complexity:   
    # postorder(right, left, root)  Append last
    # postorder is printing after you do both traversals

    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        print(traversal_list)

        return traversal_list

    # Time Complexity: 
    # Space Complexity:
    # Need a Full-Blown tranversal - reverse recursion    
    #  
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
