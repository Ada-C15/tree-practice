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
        


    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

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

# IN ORDER LIST*************************************************************
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def inorder_helper(self, current_node, inorder_list):
        if current_node == None:
            return inorder_list

        # ADD LEFT NODE FIRST
        self.inorder_helper(current_node.left, inorder_list)

        # ADD CURRENT NODE
        inorder_list.append({ 
            "key": current_node.key,
            "value": current_node.value
        })
        # ADD RIGHT NODE LAST
        self.inorder_helper(current_node.right, inorder_list)

        return inorder_list

    def inorder(self):
        inorder_list = []
        return self.inorder_helper(self.root, inorder_list)


# PRE-ORDER LIST*************************************************************

    # Time Complexity: O(log n)
    # Space Complexity: O(1)    
    def preorder_helper(self, current_node, preorder_list):
        if current_node == None:
            return preorder_list

        # ADD CURRENT NODE FIRST 
        preorder_list.append({ 
            "key": current_node.key,
            "value": current_node.value
        })
        # ADD LEFT NODE, THEN RIGHT NODE
        self.preorder_helper(current_node.left, preorder_list)
        self.preorder_helper(current_node.right, preorder_list)

        return preorder_list

    def preorder(self):
        preorder_list = []
        return self.preorder_helper(self.root, preorder_list)



# POST-ORDER LIST*************************************************************

    # Time Complexity: O(log n)
    # Space Complexity:  O(1)   
    def postorder_helper(self, current_node, postorder_list):
        if current_node == None:
            return postorder_list

        # ADD LEFT NODE, THEN RIGHT NODE 
        self.postorder_helper(current_node.left, postorder_list)
        self.postorder_helper(current_node.right, postorder_list)

        # ADD CURRENT NODE LAST 
        postorder_list.append({ 
            "key": current_node.key,
            "value": current_node.value
        })
        return postorder_list

    def postorder(self):
        postorder_list = []
        return self.postorder_helper(self.root, postorder_list)




    # Time Complexity: O(log n)
    # Space Complexity:  O(1)   
    def height_helper(self, current_node):
        if current_node == None:
            return 0
        left_node = self.height_helper(current_node.left)
        right_node = self.height_helper(current_node.right)

        return max(left_node, right_node) + 1
    
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(log n)
#   # Space Complexity: O(1)
    def bfs(self):
        tree_elements = []
        queue = []
        
    
        if self.root:
            queue.append(self.root)
        
    
        while len(queue) > 0:
            
            currNode = queue.pop(0)

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

            tree_elements.append({
                "key":currNode.key,
                "value": currNode.value})
        return tree_elements


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
