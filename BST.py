class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None

     
    
    def insert(self, value):
        """Insert a value into the BST."""
        def insert_node(node, value):
            if node is None:
                return TreeNode(value)
            if value < node.value:
                node.left = insert_node(node.left, value)
            else:
                node.right = insert_node(node.right, value)
            return node

        self.root = insert_node(self.root, value)
    
    def search(self, value):
        """Search for a value in the BST. Return True if found, else False."""
        current = self.root
        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def inorder_traversal(self):
        """Return a list of values representing in-order traversal."""
        result = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)
        
        traverse(self.root)
        return result
    
    
    def preorder_traversal(self):
        """Return a list of values representing pre-order traversal."""
        result = []

        def traverse(node):
            if node is not None:
                result.append(node.value)
                traverse(node.left)
                traverse(node.right)
        
        traverse(self.root)
        return result
    
    def postorder_traversal(self):
        """Return a list of values representing post-order traversal."""
        result = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                result.append(node.value)
        
        traverse(self.root)
        return result
    
    def delete(self, value):
        """Delete a value from the BST."""
        def find_min(node):
            while node.left is not None:
                node = node.left
            return node

        def delete_node(node, value):
            if node is None:
                return node
            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = find_min(node.right)
                node.value = temp.value
                node.right = delete_node(node.right, temp.value)
            return node

        self.root = delete_node(self.root, value)
    
# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print(bst.search(10))  # Expected output: True
print(bst.inorder_traversal())  # Expected output: [5, 10, 15]
