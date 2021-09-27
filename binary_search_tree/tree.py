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

    # Time Complexity: O(log n) - if balanced
    # Space Complexity: O(n) eventually O(log n) - recursive solution, "addresses are removed from stack when returning"
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: O(log n)
    # Space Complexity: O(n) eventually O(log n) - recursive solution, "addresses are removed from stack when returning"
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

    # Inorder helper function  
    def inorder_helper(self, current, traversal_list):
        if current != None:
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append({'key': current.key, 'value': current.value})
            self.inorder_helper(current.right, traversal_list)

    # NOTE I've been reading different arguments for recursive tree traversals online
    # and am now unsure of the most "correct" answer

    # Time Complexity: O(n) - recursive tree traversals go through each node?
    # Space Complexity: O(h) for height of tree, O(n) in worst case of skewed tree, O(log n) for nice balanced tree
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)

        return traversal_list

    # Preorder helper function  
    def preorder_helper(self, current, traversal_list):
        if current != None:
            traversal_list.append({'key': current.key, 'value': current.value})
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity: O(n)
    # Space Complexity: O(h) for height of tree, O(n) in worst case of skewed tree, O(log n) for nice balanced tree  
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)

        return traversal_list

    # Postorder helper function  
    def postorder_helper(self, current, traversal_list):
        if current != None:
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append({'key': current.key, 'value': current.value})
                

    # Time Complexity: O(n)
    # Space Complexity: O(h) for height of tree, O(n) in worst case of skewed tree, O(log n) for nice balanced tree   
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)

        return traversal_list

    # Referenced GeeksforGeeks and Sunday CS w/Ace for the following:

    # Height helper function   
    def height_helper(self, current):
        if current == None:
            return 0

        left_depth = self.height_helper(current.left)
        right_depth = self.height_helper(current.right)

        # if left_depth > right_depth:
        #     return left_depth + 1
        # else:
        #     return right_depth + 1

        return max(left_depth, right_depth) + 1

    # Time Complexity: O(n) - still visiting each node?
    # Space Complexity: O(h) for height of tree, O(n) in worst case of skewed tree, O(log n) for nice balanced tree     
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
