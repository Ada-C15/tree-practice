class TreeNode:
    # each tree node will have a key: maintin the order by ex. student id 
    # value  ex. student object 
    # we sorting by keys 
    # value is the data we are storing 
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


    # Time Complexity: O(log n) - balanced tree 
    # Space Complexity:  O (log n) - recursive approach 
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
        
        # iterative solution 
        #if self.root == None:
        #    self.root = TreeNode(key,value)
        #else:
        #    parent = None
        #    current = self.root
        #    while current != None:
        #        parent = current 
        #        if current.key > key:
        #            current = current.left
        #        else:
        #            current = current.right
        #    if parent.key > key:
        #        parent.left = TreeNode(key,value)
        #    else:
        #        parent.right = TreeNode(key, value)    
    # Time Complexity: O(log n) 
    # Space Complexity: 
    def find(self, key):
        if self.root == None:
            return None 
        else:
            current = self.root
            while current != None:
                if current.key == key:
                    return current.value
                elif current.key > key:
                    current = current.left
                else:
                    current = current.right
        
    def inorder_helper(self, current, inorder_list):
        if current != None:
            self.inorder_helper(current.left, inorder_list)
            inorder_list.append({"key": current.key,"value":current.value})
            self.inorder_helper(current.right, inorder_list)
            


    # Time Complexity: O(logn)
    # Space Complexity: O (1) - iterative approach 
    # you get all the elements in order 
    def inorder(self):
        inorder_list = []
        self.inorder_helper(self.root, inorder_list)
        return inorder_list

    # helper function for pre order
    def preorder_helper(self, current, traversal_list):
        if current != None:
            traversal_list.append({"key": current.key,"value":current.value})
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity: O(log n)
    # Space Complexity:  
    # used if you are saving a tree to an array or a file. you canread the array and get back the same 
    # root, left, right 
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, postorder_list):
        if current == None:
            return  postorder_list
        elif current != None:
            self.preorder_helper(current.left, postorder_list)
            self.preorder_helper(current.right, postorder_list)
            postorder_list.append({"key": current.key,"value":current.value})

    # Time Complexity: O(logn)
    # Space Complexity: O (1)  
    # easiest way to delete all the nodes at one time 
    def postorder(self):
        postorder_list = []
        self.postorder_helper(self.root, postorder_list)
        return postorder_list

    def height_helper(self, current):
        if current == None:
            return 0
        left_count = self.height_helper(current.left)
        right_count = self.height_helper(current.right)

        return max(left_count, right_count) + 1

    # Time Complexity: O(logn)
    # Space Complexity:  O (1)   
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(logn)
#   # Space Complexity: O (n)
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
