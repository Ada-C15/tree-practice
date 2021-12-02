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

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def add(self, key, value):
        new_node = TreeNode(key,value)
        if not self.root:
            self.root = new_node
            return 
        current = self.root
        previous = None
        while current:
            previous = current
            if current.key > new_node.key:
                current = current.left
            else:
                current = current.right
        if previous.key > new_node.key:
            previous.left = new_node
        else:
            previous.right = new_node


        
    
   
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def find(self, key):
        current_node = self.root
    
        while current_node:
            if current_node.key == key:
                return current_node.value
            elif current_node.key > key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

  
  
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def inorder(self):
        traversal_list = []
        if not self.root:
            return traversal_list
        self.inorder_helper(self.root, traversal_list)
        return traversal_list
    
    # Left, Root, Right 
    def inorder_helper(self, node, traversal_list):
        if node == None:
            return traversal_list
        self.inorder_helper(node.left, traversal_list)
        
        traversal_list.append({
            'key': node.key,
            'value' : node.value
        })
        self.inorder_helper(node.right, traversal_list)
        return traversal_list
    
   

    
    #Root, Left, Right
    def preorder_helper(self, node, traversal_list):
        
        if node == None:
            return traversal_list
        traversal_list.append({'key': node.key,
                            'value' : node.value})
           
        self.preorder_helper(node.left, traversal_list)
        self.preorder_helper(node.right, traversal_list)
        return traversal_list  
    
    # Time Complexity: O(logn)
    # Space Complexity: O(1)    
    def preorder(self):
        traversal_list = []
        if not self.root:
            return traversal_list
        self.preorder_helper(self.root, traversal_list)
        return traversal_list
    
    
   
    # Left, Right, Root
    def postorder_helper(self, node, traversal_list):
        
        if node == None:
            return traversal_list
            
        self.postorder_helper(node.left, traversal_list)
        
        self.preorder_helper(node.right, traversal_list)
        
        traversal_list.append({'key': node.key,
                            'value' : node.value})
        return traversal_list
    
    # Time Complexity: O(logn)
    # Space Complexity: O(1) 
    def postorder(self):
        traversal_list = []
        if not self.root:
            return traversal_list
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    # Time Complexity: 
    # Space Complexity:     
    # to find height we need to do DFS and store a value after each leaf is found. 
    def height_helper(self, node):
        if node == None:
            return 0
        count = 1
        left_height = self.height_helper(node.left)
        right_height = self.height_helper(node.right)
        return max(left_height,right_height)+ 1
    
    def height(self):
        if not self.root:
            return 0
        return self.height_helper(self.root)
        

    def bfs_helper(self,node,bfs_list):
        
        if node.left == None or node.right == None:
            return bfs_list
        
        self.bfs_helper(node, node.left, bfs_list)
        bfs_list.append({"key": node.left.key,
                            "value" : node.left.value})

        self.bfs_helper(node, node.right, bfs_list)
        bfs_list.append({"key": node.right.key,
                            "value" : node.right.value})

        return bfs_list
#   # Time Complexity: 
#   # Space Complexity: 
    # append root, LC,RC
    def bfs(self):
        bfs_list = []
        if not self.root:
            return bfs_list
        
        self.bfs(self.root)
        return bfs_list

    


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
