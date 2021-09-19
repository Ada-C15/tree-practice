class TreeNode:
    #key is what we are sorting values by
    def __init__(self, key, val = None):
        #without the key the key and value will be the same
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

#===========ADD==================================================================
    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        if self.root ==None:
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


#========FIND======================================================================
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

#===========INORDER==============================================================

    # Time Complexity:O(n)
    # Space Complexity: O(n)
    def inorder(self):
        result = []
        return self.inorder_helper(self.root, result)
    
    def inorder_helper(self, current, result):
        
        if current == None:
            return result
        else:
            if current.left != None:
            #recur on the left child
               self.inorder_helper(current.left,result)

            #print the data of the node
            result.append({"key": current.key, "value" : current.value})
            
            if current.right != None:
            #recur on the right child
                self.inorder_helper(current.right, result)
        
        return result


#==============PREORDER=============================================================
    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def preorder(self):
        result = []
        return self.preorder_helper(self.root, result)
    
    def preorder_helper(self, current, result):
        if current == None:
            return result
        else:
            #print the data of the node
            result.append({"key": current.key, "value" : current.value})

            if current.left != None:
            #recur  on the left child
                self.preorder_helper(current.left, result)

            if current.right != None:
            #recur on the right child
                self.preorder_helper(current.right, result)
        
        return result
    
#====================POSTORDER======================================================
    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def postorder(self):
        result = []
        return self.postorder_helper(self.root, result)
    
    def postorder_helper(self, current, result):
        if current == None:
            return result
        else:
            #recur on the left child
            if current.left != None:
                self.postorder_helper(current.left, result)
            #recur on the right child
            if self.root.right != None:
                self.postorder_helper(current.right, result)
            #print the data of the node
            result.append({"key": current.key, "value" : current.value})
        return result


#==============HEIGHT============================================================
    # Time Complexity: O(n)
    # Space Complexity: O(1) 
    def height(self):
        return self.height_helper(self.root) 
    
    def height_helper(self, current):
        if current == None:
            return 0
        
        return self.find_max(self.height_helper(current.left), self.height_helper(current.right))+1

    def find_max(self, a, b):
        if(a>=b):
            return a
        else:
            return b

#===============BREADTH FIRST SEARCH==============================================
#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        result =[]
        queue =[]
        
        if self.root:
            queue.append(self.root)
        
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)
            
            result.append({"key": current.key, "value" : current.value}) 
        return result
                    


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
