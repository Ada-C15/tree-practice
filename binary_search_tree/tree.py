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
        # print("*** add helper ", current_node)
        if current_node == None:
            return TreeNode(key, value)

        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(n), O(h)
    # Space Complexity: O(n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: O(n), O(h)
    # Space Complexity: O(n)
    def find(self, key):
        # print("*** key ", key)
        # print("root ", self.root)
        if self.root == None:
            return None

        current = self.root
        # print("current node ", current)
        while current != None:
            # print("*** current key ", current.key)
            if current.key == key:
                # print("*** value ", current.value)
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self, res=[]):
        # # tree_array = []
        # if self.root:
        #     res = self.inorder(self.root.left)
        #     res.append(self.root.key)
        #     res = self.inorder(self.root.right)
        # print("res array ", res)
        # return res
        # pass

        # print("inorder ", self.root.key)
        # print("*** helper ", self.helper_inorder(self.root))
        if self.root == None:
            return []

        return self.helper_inorder(self.root)

    def helper_inorder(self, node, tree_array=[]):
        # tree_array = []
        if node == None:
            return 

        else:
            # res.append(node.key)
            # print("helper inorder ", node.key) 
            self.helper_inorder(node.left)
            # print("node left right ", node.key)
            # res.append(node)
            # print("res array ", res)
            tree_array.append({
                'key': node.key,
                'value': node.value
            })
            self.helper_inorder(node.right)
        # print("tree array ", tree_array)
        return tree_array

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        if self.root == None:
            return []

        # print(self.helper_preorder(self.root))
        return self.helper_preorder(self.root)

    def helper_preorder(self, node, tree_array=[]):
        if node == None:
            return

        else:
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

        else:
            self.helper_postorder(node.left)
            self.helper_postorder(node.right)
            tree_array.append({
                'key': node.key,
                'value': node.value
            })

        return tree_array


    # Time Complexity: O(n)
    # Space Complexity: O(n) 
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
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
