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

    # Time Complexity:  O(log n)
    # Space Complexity: O(log n)

    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
    
        # Non-recursive version
        # if self.root == None:
        #     self.root = TreeNode(key, value)
        # else:
        #     parent = None
        #     current = self.root
        #     while current != None:
        #         parent = current
        #         if current.key > key:
        #             current = current.left
        #         else:
        #             current = current.right

        #     if parent.key > key:
        #         parent.left = TreeNode(key, value)
        #     else:
        #         parent.right = TreeNode(key, value)
        

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
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


    # Time Complexity: O(log n)
    # Space Complexity: O(n)

    def inorder_helper(self, root, node_list):
        if root == None:
            return node_list

        # ADD LEFT NODE FIRST
        self.inorder_helper(root.left, node_list)

        # ADD ROOT NODE
        node_list.append({ 
            "key": root.key,
            "value": root.value
        })
        # ADD RIGHT NODE LAST
        self.inorder_helper(root.right, node_list)

        return node_list

    def inorder(self):
        node_list = []
        return self.inorder_helper(self.root, node_list)

    # Time Complexity: O(log n)
    # Space Complexity: O(n)  
    def preorder_helper(self, root, node_list):
        if root == None:
            return node_list

        # ADD ROOT NODE FIRST 
        node_list.append({ 
            "key": root.key,
            "value": root.value
        })
        # ADD LEFT NODE, THEN RIGHT NODE
        self.preorder_helper(root.left, node_list)
        self.preorder_helper(root.right, node_list)

        return node_list

    def preorder(self):
        node_list = []
        return self.preorder_helper(self.root, node_list)

    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def postorder_helper(self, root, node_list):
        if root == None:
            return node_list

        # ADD LEFT NODE, THEN RIGHT NODE
        self.postorder_helper(root.left, node_list)
        self.postorder_helper(root.right, node_list)

        # ADD ROOT NODE LAST
        node_list.append({ 
            "key": root.key,
            "value": root.value
        })

        return node_list

    def postorder(self):
        node_list = []
        return self.postorder_helper(self.root, node_list)

    # Time Complexity: O(log n)
    # Space Complexity: O(h) with h being height of the tree
    def get_height_helper(self, node):
        if not node:
            return 0
        leftHeight = self.get_height_helper(node.left)
        rightHeight = self.get_height_helper(node.right)
        return max(leftHeight, rightHeight) + 1

    def height(self):
        return self.get_height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(log n)
#   # Space Complexity: O(n)
    def bfs(self):

        result = []
        queue = []

        if self.root:
            queue.append(self.root)

        while len(queue) > 0:

            currNode = queue.pop(0)

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

            result.append({
                "key":currNode.key,
                "value": currNode.value})
        return result


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
