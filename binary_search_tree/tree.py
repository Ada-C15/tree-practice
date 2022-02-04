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

    # Time/ Space Complexity for unbalanced tree: O(n) 
    #Time/ Space Complexity for unbalanced tree: O(log n)
    
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self._add(self.root, key, value)

    def _add(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        if key <= current_node.key:
            current_node.left = self._add(current_node.left, key, value)
        else:
            current_node.right = self._add(current_node.right, key, value)
        return current_node

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif key > current.key:
                current = current.right
            else:
                current = current.left
        return None

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        values =[]
        
        if self.root == None:
            return values

        return self._in_order(self.root, values)

    def _in_order(self, node, values):
        if node == None:
            return 

        self._in_order(node.left, values)
        values.append({
            'key': node.key,
            'value': node.value
        })
        self._in_order(node.right, values)

        return values

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        values = []

        if self.root == None:
            return values

        return self._pre_order(self.root, values)

    def _pre_order(self, node, values):
        if node == None:
            return

        values.append({
            'key': node.key,
            'value': node.value
        })
        self._pre_order(node.left, values)
        self._pre_order(node.right, values)
        
        return values

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        values = []

        if self.root == None:
            return values

        return self._post_order(self.root, values)

    def _post_order(self, node, values):
        if node == None:
            return 

        self._post_order(node.left, values)
        self._post_order(node.right, values)
        values.append({
            'key': node.key,
            'value': node.value
        })

        return values

    # Time Complexity: O(n)
    # Space Complexity: O(log n) (balanced) or O(n) for unbalanced
    def height(self):
        if self.root == None:
            return 0

        return self._height(self.root)

    def _height(self, node):
        if node == None:
            return 0

        l = self._height(node.left)
        r = self._height(node.right)

        return (1 + max(l, r))

#   # Optional Method
#   # Time Complexity: O(n^2) 
#   # Space Complexity: O(n)
##  to-do: rewrite below using dequeue or linked list for linear time

    def bfs(self):
        values = []
        queue = []
        if self.root:
            queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
            values.append({
                "key": current_node.key,
                "value": current_node.value,
            })
        return values


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
