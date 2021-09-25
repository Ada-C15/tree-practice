class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def formatted(self):
        return {"key": self.key, "value": self.value}
        


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O( log n )
    # Space Complexity: O( log n )
    def add(self, key, value = None, current = None):
        if not self.root:
            self.root = TreeNode(key, value)
            return

        if not current:
            current = self.root

        if current.key >= key:
            if current.left:
                self.add(key, value, current.left)
            else:
                current.left = TreeNode(key, value)

        if current.key < key:
            if current.right:
                self.add(key, value, current.right)
            else:
                current.right = TreeNode(key, value)

    # Time Complexity: O ( log n )
    # Space Complexity: O ( log n )
    def find(self, key):
        if not self.root:
            return None

        current = self.root
        while current.key != key:
            if current.key > key and current.left:
                current = current.left
            elif current.key < key and current.right:
                current = current.right
            elif not (current.left and current.right):
                return None

        return current.value

    # Time Complexity: O ( log n )
    # Space Complexity: O ( n )
    # left, center, right
    def inorder(self):
        if not self.root:
            return []

        return self.inorder_help(self.root)

    def inorder_help(self, current):
        ret_list = []

        if current.left:
            ret_list += self.inorder_help(current.left)

        ret_list.append(current.formatted())

        if current.right:
            ret_list += self.inorder_help(current.right)

        return ret_list

    # Time Complexity: O ( log n )
    # Space Complexity: O ( n )
    # center, left, right     
    def preorder(self):
        if not self.root:
            return []

        return self.preorder_help(self.root)

    def preorder_help(self, current):
        ret_list = []

        ret_list.append(current.formatted())

        if current.left:
            ret_list += self.preorder_help(current.left)

        if current.right:
            ret_list += self.preorder_help(current.right)

        return ret_list

    # Time Complexity: O ( log n )
    # Space Complexity: O ( n )
    # left, right, center 
    def postorder(self):
        if not self.root:
            return []

        return self.postorder_help(self.root)

    def postorder_help(self, current):
        ret_list = []

        if current.left:
            ret_list += self.postorder_help(current.left)

        if current.right:
            ret_list += self.postorder_help(current.right)

        ret_list.append(current.formatted())

        return ret_list

    # Time Complexity: O ( n )
    # Space Complexity: O ( n )
    def height(self):
        if not self.root:
            return 0

        return self.height_help(self.root)

    def height_help(self, current):
        if not current:
            return 0

        l_height = self.height_help(current.left)

        r_height = self.height_help(current.right)

        return (1 + max(l_height, r_height))



#   # Optional Method
#   # Time Complexity: O ( n )
#   # Space Complexity: O ( n )
    def bfs(self):
        if not self.root:
            return []

        process_queue = [self.root]
        index = 0

        while index < len(process_queue):
            if process_queue[index].left:
                process_queue.append(process_queue[index].left)
            if process_queue[index].right:
                process_queue.append(process_queue[index].right)
            index += 1

        return [current.formatted() for current in process_queue]


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
