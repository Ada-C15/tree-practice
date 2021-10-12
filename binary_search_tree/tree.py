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

    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def add(self, key, value = None):
        if self.root == None: 
            self.root = TreeNode(key, value)
        else: 
            self.add_helper(self.root, key, value)


    def find_helper(self, current_node, key):
        if current_node == None: 
            return None
        elif current_node.key == key: 
            return current_node.value
        elif current_node.key <= key: 
            return self.find_helper(current_node.right, key) 

        return self.find_helper(current_node.left, key) 
    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    def find(self, key):
        if self.root == None: 
            return None
        else: 
            return self.find_helper(self.root, key)


    def inorder_helper(self, current_node, node_list): 
        if current_node != None: 
            self.inorder_helper(current_node.left, node_list)
            node_list.append({"key":current_node.key,"value":current_node.value})
            self.inorder_helper(current_node.right, node_list)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        node_list = [] 
        self.inorder_helper(self.root, node_list)
        return node_list



    def preorder_helper(self, current_node, node_list): 
        if current_node != None: 
            node_list.append({"key":current_node.key,"value":current_node.value})
            self.preorder_helper(current_node.left, node_list)
            self.preorder_helper(current_node.right, node_list)
    # Time Complexity: O(n)
    # Space Complexity:  O(n)  
    def preorder(self):
        node_list = [] 
        self.preorder_helper(self.root, node_list)
        return node_list


    def postorder_helper(self, current_node, node_list): 
        if current_node != None: 
            self.postorder_helper(current_node.left, node_list)
            self.postorder_helper(current_node.right, node_list)
            node_list.append({"key":current_node.key,"value":current_node.value})
    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def postorder(self):
        node_list = [] 
        self.postorder_helper(self.root, node_list)
        return node_list


    def get_height_helper(self, current_node):
        if not current_node :
            return 0
        left_height = self.get_height_helper(current_node.left)
        right_height = self.get_height_helper(current_node.right)
        return max(left_height, right_height) + 1
    # Time Complexity: O(logN)
    # Space Complexity: O(h:heigh of the tree)    
    def height(self):
        return self.get_height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(logN)
#   # Space Complexity: O(N)
    def bfs(self):
        
        result = []
        queue = []

        if self.root:
            queue.append(self.root)

        while len(queue) > 0:

            current_node = queue.pop(0)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            result.append({
                "key":current_node.key,
                "value": current_node.value})
        return result

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
