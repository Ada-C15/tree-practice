class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        
    def __str__(self) -> str:
        return f"{self.key}: {self.value}"

class Tree:
    def __init__(self):
        self.root = None

# print all nodes in order
    def _debug(self):
        def __debug(current_node):
            if current_node == None:
                return
            __debug(current_node.left)
            print(current_node)
            __debug(current_node.right)
        __debug(self.root)

    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
            return 

    # find the parent/spot of where the new node should go
    # then set the parents' child the new node
    # current_node = {key:value}
        
        def _add(current_node, key, value):
            if current_node.key > key:
                if current_node.left == None:
                    current_node.left = TreeNode(key, value)
                else:
                    _add(current_node.left, key, value)
            else:
                if current_node.right == None:
                    current_node.right = TreeNode(key, value)
                else:
                    _add(current_node.right, key, value)

        _add(self.root, key, value)

    # Time Complexity: O(log n)
    # Space Complexity:  O(n) 

    #  2
    # 1 3
    # search for 0 - return None

    def find(self, key):
        def _find(current_node, key):
            if current_node == None:
                return None
            if current_node.key == key:
                return current_node.value
            if current_node.key > key:
                return _find(current_node.left, key)
            return _find(current_node.right, key)   
        return _find(self.root, key)

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # leftChild -  parent/root - rightChild

    # if the current node has children, check current.node.left
    # if null, check print parent, then check current.node.right

    #  2
    # 1 3
    def inorder(self):
        return_array = []
        if self.root == None:
            return return_array

        def _inorder(current_node, return_array):
            if current_node:
                _inorder(current_node.left, return_array)
                return_array.append(
                    {
                        "key": current_node.key,
                        "value": current_node.value
                    }
                )
                _inorder(current_node.right, return_array)
                return return_array

        _inorder(self.root, return_array)
        return return_array
        
    # Time Complexity: O(log n)
    # Space Complexity: O(n) 
    
    # parent/root - leftchild - rightchild     
    def preorder(self):
        return_array = []
        if self.root == None:
            return return_array

        def _preorder(current_node, return_array):
            if current_node:
                return_array.append(
                    {
                        "key": current_node.key,
                        "value": current_node.value
                    }
                )
                _preorder(current_node.left, return_array)
                _preorder(current_node.right, return_array)
                return return_array

        _preorder(self.root, return_array)
        return return_array

    # Time Complexity: O(log n)
    # Space Complexity:  O(n) 
    
    # LeftChild-RightChild-Parent/root   
    def postorder(self):
        return_array = []
        if self.root == None:
            return return_array

        def _preorder(current_node, return_array):
            if current_node:
                _preorder(current_node.left, return_array)
                _preorder(current_node.right, return_array)
                return_array.append(
                    {
                        "key": current_node.key,
                        "value": current_node.value
                    }
                )
                return return_array

        _preorder(self.root, return_array)
        return return_array


    # Time Complexity: O(1) if tree is empty. O(n) otherwise
    # Space Complexity: O(n)   
    def height(self):
        def _height(current_node):
            if not current_node:
                return 0
            leftTree = _height(current_node.left)
            rightTree = _height(current_node.right)
            return max(leftTree, rightTree) + 1
        return _height(self.root)
        
#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        queue = []
        def _bfs(current_node, queue):
            if current_node:
                if current_node.left:
                    queue.append(
                    {
                        "key": current_node.left.key,
                        "value": current_node.left.value
                    }
                )
                if current_node.right:
                    queue.append(
                    {
                        "key": current_node.right.key,
                        "value": current_node.right.value
                    }
                )
                _bfs(current_node.left, queue)
                _bfs(current_node.right, queue)
        if self.root:
            queue.append(
                {
                    "key": self.root.key,
                    "value": self.root.value
                }
            )
        _bfs(self.root, queue)
        return queue


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
