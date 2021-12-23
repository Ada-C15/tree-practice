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

    # Time Complexity: On
    # Space Complexity: O1
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: On
    # Space Complexity: O1
    def find(self, key):
        if self.root == None:
            return None
        else:
            return self.find_helper(self.root, key)

    def find_helper(self, curr, key):
        if not curr:
            return None
        elif curr.key == key:
            return curr.value 
        elif key < curr.key:
            return self.find_helper(curr.left, key)
        elif key > curr.key:
            return self.find_helper(curr.right, key)

    # Time Complexity: On
    # Space Complexity: On
    def inorder(self):
        all_ele = []
        return self.inorder_helper(self.root, all_ele)

    def inorder_helper(self, curr, all_ele):
        if not curr:
            return all_ele
        self.inorder_helper(curr.left, all_ele)
        all_ele.append({
            "key": curr.key,
            "value": curr.value})
        self.inorder_helper(curr.right, all_ele)

        return all_ele

    # Time Complexity: On
    # Space Complexity: On    
    def preorder(self):
        all_ele = []
        return self.preorder_helper(self.root, all_ele)
        
    def preorder_helper(self, curr, all_ele):
        if not curr:
            return all_ele

        all_ele.append({
            "key": curr.key,
            "value": curr.value
        })
        self.preorder_helper(curr.left, all_ele)
        self.preorder_helper(curr.right, all_ele)
    
        return all_ele

    # Time Complexity: On
    # Space Complexity: On    
    def postorder(self):
        all_ele = []
        return self.postorder_helper(self.root, all_ele)
    
    def postorder_helper(self, curr, all_ele):
        if not curr:
            return all_ele

        self.postorder_helper(curr.left, all_ele)
        self.postorder_helper(curr.right, all_ele)

        all_ele.append({
            "key": curr.key,
            "value": curr.value
        })

        return all_ele

    # # Time Complexity: On
    # # Space Complexity: O1    
    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, curr):
        if not curr:
            return 0

        left_height = self.height_helper(curr.left)
        right_height = self.height_helper(curr.right)

        return max(left_height, right_height) +1

#   # Optional Method
#   # Time Complexity: On
#   # Space Complexity: On
    def bfs(self):

        arr = []

        if not self.root:
            return arr

        root = {
            "key": self.root.key,
            "value": self.root.value}

        temp = [self.root]
        arr.append(root)

        while len(temp) > 0:
            curr = temp[0]
        
            if curr.left:
                temp.append(curr.left)
                arr.append({
                    "key": curr.left.key,
                    "value": curr.left.value})
            
            if curr.right:
                temp.append(curr.right)
                arr.append({
                    "key": curr.right.key,
                    "value": curr.right.value})

            temp.remove(curr)
        
        return arr

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
