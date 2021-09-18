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


    # Time Complexity:O(n)
    # Space Complexity: O(n)
    def inorder(self):
        if self.root != None:
            if self.root.left != None:
            #recur on the left child
                self.inorder(self.root.left)

            #print the data of the node
            print(self.root.val)
            
            if self.root.right != None:
            #recur on the right child
                self.inorder(self.root.right)
        

    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def preorder(self):
        
        if self.root != None:
            #print the data of the node
            print(self.root.val)

            #recur  on the left child
            self.preorder(self.root.left)

            #recur on the right child
            self.preorder(self.root.right)



    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def postorder(self):
        if self.root != None:

            #recur  on the left child
            self.preorder(self.root.left)
            #recur on the right child
            self.preorder(self.root.right)
            #print the data of the node
            print(self.root.val)

    # Time Complexity: O(n)
    # Space Complexity: O(1)  
    def height(self):
        if self.root == None:
            return 0
        
        return self.find_max(self.height(self.root.left), self.height(self.root.right))+1

    def find_max(self, a, b):
        if(a>=b):
            return a
        else:
            return b

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
