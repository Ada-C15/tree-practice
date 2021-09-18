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

    # Time Complexity: O(n), O(h)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: O(n), O(h)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None

        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        if self.root == None:
            return []

        return self.helper_inorder(self.root)

    def helper_inorder(self, node, tree_array=[]):
        if node == None:
            return 

        self.helper_inorder(node.left)
        tree_array.append({
            'key': node.key,
            'value': node.value
        })
        self.helper_inorder(node.right)

        return tree_array

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        if self.root == None:
            return []

        return self.helper_preorder(self.root)

    def helper_preorder(self, node, tree_array=[]):
        if node == None:
            return

        tree_array.append({
            'key': node.key,
            'value': node.value
        })
        self.helper_preorder(node.left)
        self.helper_preorder(node.right)
        
        return tree_array


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        if self.root == None:
            return []

        return self.helper_postorder(self.root)

    def helper_postorder(self, node, tree_array=[]):
        if node == None:
            return 

        self.helper_postorder(node.left)
        self.helper_postorder(node.right)
        tree_array.append({
            'key': node.key,
            'value': node.value
        })

        return tree_array


    # Time Complexity: O(n)
    # Space Complexity: O(1) 
    def height(self):
        if self.root == None:
            return 0

        print("height ", self.helper_height(self.root))
        return self.helper_height(self.root)

    def helper_height(self, node):
        if node == None:
            return 0

        left = self.helper_height(node.left)
        right = self.helper_height(node.right)

        return max(left, right) + 1


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n), O(w)
    def bfs(self):
        if self.root == None:
            return []
        
        return self.helper_bf(self.root)

    def helper_bf(self, node, tree_array=[]):
        if node == None:
            return
        
        queue = []
        queue.append(node)

        while len(queue) != 0:
            current_node = queue.pop(0)
            tree_array.append({
                'key': current_node.key,
                'value': current_node.value
            })

            if current_node.left != None:
                queue.append(current_node.left)
            
            if current_node.right != None:
                queue.append(current_node.right)

        return tree_array


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
