from typing import Counter


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


    # Time Complexity:O(log n) 
    # Space Complexity:O(1)
    def add(self, key, value = None):
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
    def inorder_helper_f(self,current_node, in_order_list):
        if current_node == None:
            return in_order_list
        
        self.inorder_helper_f(current_node.left, in_order_list)
        in_order_list.append({"key": current_node.key,"value":current_node.value})
        self.inorder_helper_f(current_node.right, in_order_list)
        return in_order_list

    # Time Complexity: O(log n) 
    # Space Complexity: O(1)
    def inorder(self):
        in_order_list = []
        
        return self.inorder_helper_f(self.root,in_order_list)
        

    def preorder_helper_f(self,current_node,preorder_list):
        if current_node == None:
            return  preorder_list
        
        preorder_list.append({"key": current_node.key,"value":current_node.value})

        self.preorder_helper_f(current_node.left, preorder_list)
        self.preorder_helper_f(current_node.right, preorder_list)
        return preorder_list


    # Time Complexity:O(log n) 
    # Space Complexity: O(1)   
    def preorder(self):
        preorder_list = []

        return self.preorder_helper_f(self.root,preorder_list)

    def postorder_helper_f(self,current_node,  post_order_list):
        if current_node == None:
            return  post_order_list

        self.postorder_helper_f(current_node.left, post_order_list)
        self.postorder_helper_f(current_node.right, post_order_list)

        post_order_list.append({"key": current_node.key,"value":current_node.value})
        
        return post_order_list
    # Time Complexity: O(log n)
    # Space Complexity: O(1)     
    def postorder(self):
        post_order_list = []

        return self.postorder_helper_f(self.root,post_order_list)

    def height_helper_f(self, current_node):
        # current_node = self.root
        if current_node == None:
            return 0

        left_count = self.height_helper_f(current_node.left)
        right_count = self.height_helper_f(current_node.right)

        return max(left_count, right_count) + 1
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def height (self):
        return self.height_helper_f(self.root)

#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        ans = []
        queue = []
        
    
        # Return Null if the tree is empty
        if self.root:
            queue.append(self.root)
        
    
        while len(queue) > 0:
            
            currNode = queue.pop(0)

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

            ans.append({"key":currNode.key,"value": currNode.value})
        return ans

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
