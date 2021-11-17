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
        # self.treeheight = 0

    # Time Complexity: 
    # Space Complexity: 
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

        # if key is None:
        #     return TreeNode(key,value)
        # else:
        #     if key.val == key:
        #         return key
        #     elif key.val < key:
        #         key.right = add(TreeNode.right, key)
        #     else:
        #         key.left = add(root.left, key)
        # return root
        

    def create_dict(self, TreeNode):
        return { "key": TreeNode.key,
                 "value": TreeNode.value }
        

    # Time Complexity: 
    # Space Complexity: 
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


    # Time Complexity: 
    # Space Complexity: 

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

    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        node_list = []

        if self.root == None:
            return []
        self.preorder_traverse(self.root, node_list)  
        return node_list

     

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        node_list = []

        if self.root == None:
            return []
        self.postorder_traverse(self.root, node_list)  
        return node_list
        

    # Time Complexity: 
    # Space Complexity:     
    def height(self):   
        # if self.root == None:
        #     self.height = height
        #     return self.height
       
        if self.root == None:
            return 0
            
        

       

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
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



