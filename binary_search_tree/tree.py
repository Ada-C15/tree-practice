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

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key,value)
        current = self.root

        while True:
            if self.root.key == key:
                break
            elif current.key > key:
                if current.left != None:
                    current = current.left
                else:
                    current.left = TreeNode(key,value)
                    break
            elif current.key < key:
                if current.right != None:
                    current = current.right
                else:
                    current.right = TreeNode(key,value)
                    break
        # return self.root
        # if current ==
        

    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        def helper(node):
            if node == None:
                return []
            left_part= helper(node.left) 
            middle_part = [{"key":node.key,"value":node.value}]
            right_part = helper(node.right)
            result = left_part + middle_part + right_part
            return result

        return helper(self.root)
        
        
    
    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        def helper( node):
            if node == None:
                return []
            left_part= helper(node.left) 
            middle_part = [{"key":node.key,"value":node.value}]
            right_part = helper(node.right)
            result = middle_part + left_part +  right_part
            return result

        return helper(self.root)

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        def helper( node):
            if node == None:
                return []
            left_part= helper(node.left) 
            middle_part = [{"key":node.key,"value":node.value}]
            right_part = helper(node.right)
            result = left_part +  right_part + middle_part 
            return result

        return helper(self.root)

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        def helper(node):
            if node == None:
                return 0
            left_part= helper(node.left)
            right_part = helper(node.right)
            result = max(left_part, right_part) + 1
            return result
        return helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        if self.root == None:
            return []

        queue = []
        leveled_order = [{ 
                    "key" : self.root.key, 
                    "value":self.root.value
                    }]

        queue.append(self.root)
        while queue != []:
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
                leveled_order.append({ 
                    "key" : temp.left.key, 
                    "value": temp.left.value
                    })
            if temp.right:
                queue.append(temp.right)
                leveled_order.append({ 
                    "key" : temp.right.key, 
                    "value": temp.right.value
                    })
    
        return leveled_order


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
