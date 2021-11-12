
# Unbalanced: A BST where each node has 0 or 1 children (it looks like a linked list)
# Balanced: A tree where the the level of any two leaves differs by at most 1 node.

# When you double the number of nodes, the height increases by 1.
# ~ O(log n)
# 1 node  = h 1
# 2 nodes = h 2
# 4 nodes = h 3
# 8 nodes = h 4

#===================================================================
class TreeNode:
    def __init__(self, key, val = None):
        """
        Each tree node is going to have a KEY and a VALUE.
        The key is whatever sorting ID we're using. 
        
        The value is set to None by default so that if no value
        gets passed in, then the value is just set to the key.
        The left and right attributes for each node are also
        None by default, but these don't get passed in.   
        """
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
    
    # def add(self, key, value = None):
    #     # if there is no root node, create one and assign it to the root
    #     if self.root == None:
    #         self.root = TreeNode(key, value)
    #     # if there is a root node, 
    #     else:
    #         parent = None
    #         current = self.root
    #         while current != None:
    #             parent = current
    #             # `key` is the number we've been given and is what we're
    #             #  using to guide where in the tree to place the node 
    #             # `current.key` is the node we're currently stopped on 
    #             if key < current.key: #...if true, need to go left 
    #                 current = current.left
    #             else: #...if false, need to go right
    #                 current = current.right
    #         if key < parent.key:
    #             parent.left = TreeNode(key, value)
    #         else:
    #             parent.right = TreeNode(key, value)

    def add_helper(self, current_node, key, value):
        #=======BASE CASE!=====================================
        if current_node == None: # if the node is empty
            return TreeNode(key, value) # make one and return it

        #=======RECURSIVE CALLS!===============================
        if key <= current_node.key: # if we have some nodes and the passed-in key is less than the current node's key
            current_node.left = self.add_helper(current_node.left, key, value) 
        else:
            current_node.right = self.add_helper(current_node.right, key, value)

        return current_node

    def add(self, key, value = None):
        """
        Note: Remember that these methods operate on the nodes of the whole tree,
        not a single node itself i.e. Tree.add(), not TreeNode.add()
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) for a balanced tree 
        """
        # if there is no root node, create one and assign it to the root
        if self.root == None:
            self.root = TreeNode(key, value)
        # if there is a root node, 
        else:
            self.add_helper(self.root, key, value)

#===================================================================
    def find(self, key):
        """
        Note: Taking in a key (index marker) and want to get the node value associated
        with that key, and return None if there is no node there

        Time Complexity: O(log n)
        Space Complexity: O(1) because you're not changing the tree
        """
        # 1. If there are no nodes in the tree, return None:
        if self.root == None:
            return None
        
        # 2. If there is at least one node, start the current node at the root
        current = self.root
        while current:
            # if you find something at that key, return the node's value
            if current.key == key:
                return current.value
            # otherwise, keep going
            elif key > current.key:
                current = current.right
            else:
                current = current.left

        # 3. If no node exists at that key, bail!
        return None

#===================================================================

    def inorder_helper(self, root, nodes_in_order):
        """
        Note: Depth first: Left -> Root -> Right
        """
        #=======BASE CASE!=====================================
        if root == None:
            return 
        #=======RECURSIVE CALLS!===============================
        self.inorder_helper(root.left, nodes_in_order) # traverse the left subtree
        nodes_in_order.append({"key": root.key, "value": root.value}) # visit the root node
        self.inorder_helper(root.right, nodes_in_order) # traverse the right subtree
        return 

    def inorder(self):
        """
        Note: Depth first: Left -> Root -> Right
        In other words - this method should return an array of nodes in ascending order by key

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # 1. If there are no nodes in the tree, return empty list:
        if self.root == None:
            return []

        nodes_in_order = []
        self.inorder_helper(self.root, nodes_in_order)

        return nodes_in_order

#===================================================================

    def preorder_helper(self, root, nodes_preorder):
        """
        Note: Depth first: Root -> Left -> Right
        """
        #=======BASE CASE!=====================================
        if root == None:
            return 

        #=======RECURSIVE CALLS!===============================
        nodes_preorder.append({"key": root.key, "value": root.value}) # visit the root node
        self.preorder_helper(root.left, nodes_preorder) # traverse the left subtree
        self.preorder_helper(root.right, nodes_preorder) # traverse the right subtree
        return 

    def preorder(self):
        """
        Note: Depth first: Root -> Left -> Right

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # 1. If there are no nodes in the tree, return empty list:
        if self.root == None:
            return []
            
        nodes_preorder = []
        self.preorder_helper(self.root, nodes_preorder)

        return nodes_preorder

#===================================================================

    def postorder_helper(self, root, nodes_postorder):
        """
        Note: Depth first: Left -> Right -> Root
        """
        #=======BASE CASE!=====================================
        if root == None:
            return 
        #=======RECURSIVE CALLS!===============================
        self.postorder_helper(root.left, nodes_postorder) # traverse the left subtree
        self.postorder_helper(root.right, nodes_postorder) # traverse the right subtree
        nodes_postorder.append({"key": root.key, "value": root.value}) # visit the root node
        return 

    def postorder(self):
        """
        Note: Depth first: Left -> Right -> Root

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # 1. If there are no nodes in the tree, return empty list:
        if self.root == None:
            return []

        nodes_postorder = []
        self.postorder_helper(self.root, nodes_postorder)

        return nodes_postorder

#===================================================================
    def max_height_helper(self, root, height):
        
        if root == None:
            return height

        # Otherwise return 1 plus the maximum of the heights of the 
        # right and left subtrees
        left_height = 1 + self.max_height_helper(root.left, height)
        right_height = 1 + self.max_height_helper(root.right, height)

        if left_height > right_height:
            return left_height
        else:
            return right_height

    def height(self):
        """
        Note: Have to iterate through every node, and the recursive stack size 
        will be directly proportional to the number of nodes

        Time Complexity: O(n) 
        Space Complexity: O(log n) for a balanced tree 
        """

        if self.root != None:
            return self.max_height_helper(self.root, 0)
        return 0

#===================================================================
#   Optional Method
    def bfs(self):
        """
        Note: 

        Time Complexity: 
        Space Complexity:  
        """
        pass

#===================================================================

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"

#=============================================================================
# HOW TO MANUALLY TEST TREES

# 1. Have to create a tree, which is empty by default
# with a root of None 
# tree = Tree()

# 2. Confirm tree is empty before adding
# print(tree.root == None)

# 3. Start adding notes
# tree.add(5)
# tree.add(7)
# tree.add(10)
# tree.add(3)
# tree.add(4)

# 4. Might be helpful at this stage to draw what your tree SHOULD look like

# 5. Now right True print statements to check the structure of tree
# print(tree.root.key == 5)
# print(tree.root.right.key == 7)
# print(tree.root.right.right.key == 10)
# print(tree.root.left.key == 3)
# print(tree.root.left.right.key == 4) 

#=============================================================================
tree = Tree()
# tree.add(1, "frog")
# tree.add(2, "chichi")
# tree.add(3, "ring-tailed lemur")
# tree.add(4, "bat")
# tree.add(5, "Ido")
tree.add(1, 54)
tree.add(2, 86)
tree.add(3, 22)
tree.add(4, 85)
tree.add(5, 99)
print(tree.inorder())
print(tree.height())