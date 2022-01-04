class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.value = val
        self.key = key
        self.left = None
        self.right = None
        # self.val = key
        


class Tree:
    def __init__(self, height = None):
        self.root = None
        self.nodes = []
        #hold for the bfs
        self.queque = []
        # self.treeheight = 0
        self.bfs_nodes = []

    # Time Complexity: O(n) because looping through all the nodes
    # Space Complexity: O(n) because you need to add a node for each key, value
    def add(self, key, value = None):
        
        if self.root == None:
            self.root = TreeNode(key,value)
        else:
            parent = None
            current = self.root
            while (current !=None):
                parent = current
                if current.key > key:
                    current = current.left
                else:
                    current = current.right
            if parent.key > key:
                parent.left = TreeNode(key,value)
            else:
                parent.right = TreeNode(key,value)
        

    def create_dict(self, TreeNode):
        return { "key": TreeNode.key,
                 "value": TreeNode.value }
        

    # Time Complexity: log(n) because we are examining only half of the nodes
    # Space Complexity: O(1) because we are not allocating any memory
    # self refers to object the class is making
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


    # Time Complexity:  O(N).  Since it is recursive it is O(N) because the stack size will depend on the input size.  Behind the scenes a new stack frame is created to hold the return address and variables you create in the new call.
    # Space Complexity: 0(N)  depends on input size

    # first go to left 
  
    # add to the list 
    # go to the right
    
    

        
    def preorder_traverse(self, node, node_list): 
        node_list.append(self.create_dict(node))
        if node.left!=None:
            self.preorder_traverse(node.left, node_list)
        if node.right!=None:
            self.preorder_traverse(node.right, node_list)

    def postorder_traverse(self, node, node_list): 
        if node.left!=None:
            self.postorder_traverse(node.left, node_list)
        if node.right!=None:
            self.postorder_traverse(node.right, node_list)
        node_list.append(self.create_dict(node))

    def inorder_traverse(self, node, node_list): 
        if node.left!=None:
            self.inorder_traverse(node.left, node_list)
        node_list.append(self.create_dict(node))
        if node.right!=None:
            self.inorder_traverse(node.right, node_list)
        
       
        
    def inorder(self):
        node_list = []
        if self.root == None:
            return []
        self.inorder_traverse(self.root, node_list)  
        return node_list

    # Time Complexity: 0(N)
    # Space Complexity: Space Complexity: 0(N)  depends on input size    
    def preorder(self):
        node_list = []

        if self.root == None:
            return []
        self.preorder_traverse(self.root, node_list)  
        return node_list

     

    # Time Complexity: 0(N)
    # Space Complexity: depends on input size        
    def postorder(self):
        node_list = []

        if self.root == None:
            return []
        self.postorder_traverse(self.root, node_list)  
        return node_list
        

    # Time Complexity: 0(1) constant time
    # Space Complexity:  0(1)   
    def height(self):   
        return self.height_helper(self.root)
        
 
 
    def height_helper(self, current):
    
        # Check if the binary tree is empty
        if current is None:
            # If TRUE return 0
            return 0 
        # Recursively call height of each node
        leftHeight = self.height_helper(current.left)
        rightHeight = self.height_helper(current.right)
        my_max = max(leftHeight, rightHeight) 
        # Return max(leftHeight, rightHeight) at each iteration
        return my_max + 1
    


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
#   Create function processing root
#   If null empty array
#   Create a array use only the root then Loop 
#   Make an array empty but will contain dictionaries at end
#   While que not empty 
#   Before pop head get info of current node add dict to the final array 
#   Encue the children insert at the tail
#   https://www.geeksforgeeks.org/level-order-tree-traversal/
    def bfs(self):
       
        # if self.root is None:
        #     return [{}]

        if self.root is None:
            return 
        self.queque = [self.root]

        while len(self.queque) > 0:
            cur_node = self.queque.pop(0)
            my_dict_of_current_node = self.create_dict(cur_node)        
            self.bfs_nodes.append(my_dict_of_current_node)      

            if cur_node.left is not None:
                self.queque.append(cur_node.left)

            if cur_node.right is not None:
                self.queque.append(cur_node.right) 

        return self.bfs_nodes
          
        
        # while self.current != None:
        

#   # Useful for printing
    def to_str(self):
        return f"{self.inorder()}"

# tree = Tree()
# print(tree.root == None)
# tree.add(5, "Peter")
# tree.add(7,"Ada")
# tree.add(10)
# tree.add(3)
# tree.add(4)

# print(tree.root.key == 5)
# print(tree.root.right.key == 7)
# print(tree.root.right.right.key == 10)
# print(tree.root.left.key ==3)
# print(tree.root.left.right.key ==4)

# print(tree.find(5) == "Peter")
# print(tree.find(7) == "Ada")
# print(tree.find(4) == 4)



