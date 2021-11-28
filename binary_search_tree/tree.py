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

    # Time Complexity: O(log n) if balanced
    # Space Complexity: O(1)

    def add(self, key, value = None):
        new_node = TreeNode(key, value)

        if self.root == None:
            self.root = new_node
            return self.root

        return self.__add_helper(self.root, new_node)

    def __add_helper(self, current, new_node):
        if not current:
            return new_node

        if new_node.key <= current.key:
            current.left = self.__add_helper(current.left, new_node)
        else:
            current.right = self.__add_helper(current.right, new_node)
        
        return current

    def add_iterative(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key=key, val=value)
            return self.root

        current_node = self.root

        while current_node:
            if key <= current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = TreeNode(key=key, val=value)
                    return current_node.left
            elif key > current_node.key:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = TreeNode(key=key, val=value)
                    return current_node.right

    # Time Complexity: O(log n) if balanced
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None

        return self.__find_helper(self.root, key)

    def __find_helper(self, root, key):
        if not root:
            return None
        
        if root.key == key:
            return root.value
        elif key < root.key:
            return self.__find_helper(root.left, key)
        else:
            return self.__find_helper(root.right, key)


    def find_iterative(self, key):
        current_node = self.root
        while current_node:
            if current_node.key == key: 
                return current_node.value
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None
        

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        if self.root == None:
            return []

        result = []

        return self.__inorder_helper(self.root, result)

    def __inorder_helper(self, root, result):
        if root:
            self.__inorder_helper(root.left, result)
            result.append(self.to_dict(root))
            self.__inorder_helper(root.right, result)

        return result



    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        if self.root == None:
            return []

        result = []

        return self.__preorder_helper(self.root, result)

    def __preorder_helper(self, root, result):
        if root:
            result.append(self.to_dict(root))
            self.__preorder_helper(root.left, result)
            self.__preorder_helper(root.right, result)

        return result

    def preorder_iterative(self):
        if not self.root:
            return []

        result = []
        stack = []
        stack.append(self.root)

        while len(stack) > 0:
            root = stack.pop()
            result.append(self.to_dict(root))
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        if not self.root:
            return []
            
        result = []

        return self.__postorder_helper(self.root, result)

    def __postorder_helper(self, root, result):
        if root:
            self.__postorder_helper(root.left, result)
            self.__postorder_helper(root.right, result)
            result.append(self.to_dict(root))

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):
        if self.root == None:
            return 0

        return self.__height_helper(self.root)
        
    def __height_helper(self, root):
        if not root:
            return 0

        max_height = max(self.__height_helper(root.left), self.__height_helper(root.right)) + 1

        return max_height


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        if self.root == None:
            return []
        
        bfs = []
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            bfs.append(self.to_dict(current))

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return bfs



#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"

    def to_dict(self, node):
        return {
            'key': node.key,
            'value': node.value
        }