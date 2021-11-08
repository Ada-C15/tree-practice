class TreeNode:
    # sorting by key 
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

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
        
    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        # key = 7 , value = "Ada"
        # we are adding by key
        if key  <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # # Not recursive 
    # # Time Complexity: O(log n)
    # # Space Complexity: O(1)
    # def find(self, key):
    #     current = self.root
    #     while current:
    #         if key < current.key:
    #             current = current.left
    #         elif key > current.key:
    #             current = current.right
    #         else:
    #             return current.value
    #     return None

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        else: 
            return self.find_helper(self.root, key) 

    def find_helper(self, current_node, key): 
        if current_node == None:
            return None

        if current_node.key == key:
            return current_node.value
        elif current_node.key <= key:
            return self.find_helper(current_node.right, key)
        else:
            return self.find_helper(current_node.left, key)
    

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        nodes_in_tree = []
        
        if self.root == None:
            return nodes_in_tree

        return self.helper_inorder(self.root, nodes_in_tree)

    def helper_inorder(self, node, nodes_in_tree):
        if node == None:
            return 

        self.helper_inorder(node.left, nodes_in_tree)
        nodes_in_tree.append({
            'key': node.key,
            'value': node.value
        })
        self.helper_inorder(node.right, nodes_in_tree)

        return nodes_in_tree

    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        nodes_in_tree = []

        if self.root == None:
            return nodes_in_tree

        return self.helper_preorder(self.root, nodes_in_tree)

    def helper_preorder(self, node, nodes_in_tree):
        if node == None:
            return

        nodes_in_tree.append({
            'key': node.key,
            'value': node.value
        })
        self.helper_preorder(node.left, nodes_in_tree)
        self.helper_preorder(node.right, nodes_in_tree)
        
        return nodes_in_tree
    

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        nodes_in_tree = []

        if self.root == None:
            return nodes_in_tree

        return self.helper_postorder(self.root, nodes_in_tree)

    def helper_postorder(self, node, nodes_in_tree):
        if node == None:
            return 

        self.helper_postorder(node.left, nodes_in_tree)
        self.helper_postorder(node.right, nodes_in_tree)
        nodes_in_tree.append({
            'key': node.key,
            'value': node.value
        })

        return nodes_in_tree


    # Time Complexity: O(n)
    # Space Complexity: O(1) 
    def height(self):
        if self.root == None:
            return 0

        return self.helper_height(self.root)

    def helper_height(self, node):
        if node == None:
            return 0

        left = self.helper_height(node.left)
        right = self.helper_height(node.right)

        return max(left, right) + 1


    # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        nodes_in_tree = []

        if self.root == None:
            return nodes_in_tree
        
        return self.helper_bf(self.root, nodes_in_tree)

    def helper_bf(self, node, nodes_in_tree):
        if node == None:
            return
        
        queue = []
        queue.append(node)

        while len(queue) != 0:
            current_node = queue.pop(0)
            nodes_in_tree.append({
                'key': current_node.key,
                'value': current_node.value
            })

            if current_node.left != None:
                queue.append(current_node.left)
            
            if current_node.right != None:
                queue.append(current_node.right)

        return nodes_in_tree


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
