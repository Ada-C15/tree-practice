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

    def add_helper(self, current_node, new_node):
        if current_node == None:
            return new_node

        if new_node.key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, new_node)
        else:
            current_node.right = self.add_helper(current_node.right, new_node)

        return current_node

    # # Time Complexity: O(log n)
    # # Space Complexity: O(1)
    def add(self, key, value=None):
        node = TreeNode(key, value)
        if self.root == None:
            self.root = node
            return

        self.add_helper(self.root, node)

    def find_helper(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif key < current.key:
            return self.find_helper(current.left, key)

        return self.find_helper(current.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        return self.find_helper(self.root, key)

    def inorder_helper(self, current, traversal_list):
        if current != None:
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append({'key': current.key, 'value': current.value})
            self.inorder_helper(current.right, traversal_list)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        return traversal_list

    def preorder_helper(self, current, traversal_list):
        if current != None:
            traversal_list.append({'key': current.key, 'value': current.value})
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, traversal_list):
        if current != None:
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append({'key': current.key, 'value': current.value})

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    def height_helper(self, current):
        if current == None:
            return 0
        left = self.height_helper(current.left)
        right = self.height_helper(current.right)

        return max(left, right) + 1

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def height(self):
        return self.height_helper(self.root)

#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        # checks that there is a tree
        traversal_list = []

        if self.root == None:
            return traversal_list
        else:
            traversal_list.append({'key': self.root.key, 'value': self.root.value})

        # initiates queue to keep track of searched nodes
        queue = [self.root]

        # dequeues the first node and stores in current to check for child nodes
        while len(queue) > 0:
            current = queue.pop(0)

            # if the current node has a left or a right child, append it to the back of the queue
            if current.left != None:
                queue.append(current.left)
                traversal_list.append({'key': current.left.key, 'value': current.left.value})

            # checks for a right child in a separate if statement, because if there is a left and a right, we want to append both
            if current.right != None:
                queue.append(current.right)
                traversal_list.append({'key': current.right.key, 'value': current.right.value})

        return traversal_list

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
