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

        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    #Iterative solution
    #Time complexity: 0(log n) -  if balanced
    #Space complexity: 0(1) - will always only increase by 1 if we add
    # if self.root == None:
    #     self.root = TreeNode(key, value=None)
    # else:
    #     previous = None
    #     current = self.root

    #     while current != None:
    #         previous = current
    #         if key <= current.key:
    #             current = current.left
    #         else:
    #             current = current.right
        
    #     if key <= previous.key:
    #         parent.left == TreeNode(key, value)
    #     else:
    #         parent.right = TreeNode(key, value)


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

        return None


    def inorder_helper(self):
        pass

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
    #left, root, right
        nodes_array = []
        current =self.root

        if self.root == None:
            return []

        while current != None:
            nodes_array = self.inorder(current.left)
            nodes_array.append(current.value)
            nodes_array = nodes_array + self.inorder(current.right) 
        return nodes_array 

    def preorder_helper(self, current, nodes_array):
        if current != None:
            nodes_array.append({"key": current.key, "value": current.value})
            self.preorder_helper(current.left, nodes_array)
            self.preorder_helper(current.right, nodes_array)
        
        #or in a more recognizably recursive format 
        #if current = none:
        #return None
        # nodes_array.append({"key": current.key, "value": current.value})
        # self.preorder_helper(current.left, nodes_array)
        # self.preorder_helper(current.right, nodes_array)

        
    
    # Time Complexity: 
    # Space Complexity:  
    def preorder(self):
    #root, left, right
        nodes_array = []
        self.preorder_helper(self.root, nodes_array)
        return nodes_array


    # Time Complexity: 
    # Space Complexity:      
    def postorder(self):
    #left, right, root
        nodes_array = []
        if self.root != None:
            nodes_array.append(self.postorder(self.root.left))
            nodes_array.append(self.postorder(self.root.right))
        return nodes_array

    def height_helper(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
    def height(self):

        root = self.root
        if root == None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))
        
        #other possibilites...
        # left = self.height(root.left)
        # right = self.height(root.right)

        # if left > right:
        #     return left + 1
        # else:
        #     return right + 1

        #concept:
        #if the current root is nil/none 
        #return None 
        #else 
        #return 1 + the maximum of the heoght of the left and right subtrees


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"

tree = Tree()
# print(tree.root == None)
tree.add(5, 'Ruthie')
tree.add(7, 'Ada')
tree.add(10)
tree.add(3)
tree.add(4)

# print(tree.root.key == 5)
# print(tree.root.right.key == 7)
# print(tree.root.right.right.key == 10)
# # print(tree.root.left.key == 3)
# print(tree.root.left.right.key == 4)

# print(tree.find(5) == "Ruthie")
# print(tree.find(7) == 'Ada')
# print(tree.find(4) == 4)
print(tree.height_helper())


# def delete_node(self, key):
#     #search for value
#     #if value == leaf_value:
#         #delete leaf_value
#     #else if value has 1 child:
#         #bypass value(change pointer to skip value to delete) 
#     #else replace v with successor