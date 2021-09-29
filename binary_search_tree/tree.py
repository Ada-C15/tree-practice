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

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
            return
        self.add_node(self.root, new_node)

    def add_node(self, current, new_node):
        if current == None:
            return new_node
        if  new_node.key <= current.key:
            current.left = self.add_node(current.left, new_node)
        else:
            current.right = self.add_node(current.right, new_node)
        return current

    # Time Complexity: O(n)
    # Space Complexity: O(n)     
    def find(self, key):
        return self.find_node(self.root, key)
    
    def find_node(self,current,key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self.find_node(current.left, key)

        return self.find_node(current.right, key)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        node_list = []
        if not self.root:
            return node_list
        return self.inorder_traverse(self.root, node_list)
    
    def inorder_traverse(self, root, node_list):
        if root:
            self.inorder_traverse(root.left, node_list)
            node_list.append({"key": root.key, "value": root.value})
            self.inorder_traverse(root.right, node_list)
            return node_list
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self):
        node_list = []
        if not self.root:
            return node_list
        return self.preorder_traverse(self.root, node_list)
    
    def preorder_traverse(self, root, node_list):
        if root:
            node_list.append({"key": root.key, "value": root.value})
            self.preorder_traverse(root.left, node_list)
            self.preorder_traverse(root.right, node_list)
            return node_list
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def postorder(self):
        node_list = []
        if not self.root:
            return node_list
        return self.postorder_traverse(self.root, node_list)
    
    def postorder_traverse(self, root, node_list):
        if root:
            self.postorder_traverse(root.left, node_list)
            self.postorder_traverse(root.right, node_list)
            node_list.append({"key": root.key, "value": root.value})
            return node_list

    # Time Complexity: O(n)
    # Space Complexity: O(h) (h is height of the tree)  
    def height(self):
        return self.get_height(self.root)
    
    def get_height(self, node):
        if not node:
            return 0
        leftHeight = self.get_height(node.left)
        rightHeight = self.get_height(node.right)
        return max(leftHeight, rightHeight) + 1
        
        


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(h) (h is height of the tree) 
    def bfs(self):
        return self.bfs_traversal(self.root)
    
    def bfs_traversal(self, node):
        if not node:
            return []
        node_queue = [node]
        result = [{"key":node.key, "value":node.value}]
        while len(node_queue) > 0:
            current_node = node_queue.pop(0)
            if current_node.left:
                node_queue.append(current_node.left)
                result.append({"key": current_node.left.key, "value": current_node.left.value})
            if current_node.right:
                node_queue.append(current_node.right)
                result.append({"key": current_node.right.key, "value": current_node.right.value})
        return result

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
