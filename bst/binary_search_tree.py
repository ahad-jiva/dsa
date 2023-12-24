from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        return self.root is None

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.search_helper(self.root, key)

    def search_helper(self, node, target_key):
        if node is not None:
            if node.key == target_key:
                return True
            elif node.key < target_key:
                return self.search_helper(node.right, target_key)
            elif node.key > target_key:
                return self.search_helper(node.left, target_key)
        return False

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            self.root = TreeNode(key, data)
        return self.insert_helper(self.root, key, data)

    def insert_helper(self, node, inserted_key, inserted_data):
        if node.key == inserted_key:
            node.data = inserted_data
        elif node.key < inserted_key:
            if node.right is None:
                node.right = TreeNode(inserted_key, inserted_data)
            return self.insert_helper(node.right, inserted_key, inserted_data)
        elif node.key > inserted_key:
            if node.left is None:
                node.left = TreeNode(inserted_key, inserted_data)
            return self.insert_helper(node.left, inserted_key, inserted_data)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.find_min_helper(self.root)

    def find_min_helper(self, node):
        if (node.left is not None) and node.key > node.left.key:
            return self.find_min_helper(node.left)
        min_tuple = (node.key, node.data)
        return min_tuple

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        return self.find_max_helper(self.root)

    def find_max_helper(self, node):
        if (node.right is not None) and node.right.key > node.key:
            return self.find_max_helper(node.right)
        max_tuple = (node.key, node.data)
        return max_tuple

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        elif self.root.right is None and self.root.left is None:
            return 0
        return self.tree_height_helper(self.root)

    def tree_height_helper(self, node):
        if node.right is not None and node.left is not None:
            return 1 + max(self.tree_height_helper(node.left), self.tree_height_helper(node.right))
        elif node.right is None and node.left is not None:
            return 1 + self.tree_height_helper(node.left)
        elif node.right is not None and node.left is None:
            return 1 + self.tree_height_helper(node.right)
        return 0

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.inorder_list_helper(self.root)

    def inorder_list_helper(self, node):
        if node is not None:
            return self.inorder_list_helper(node.left) + [node.key] + self.inorder_list_helper(node.right)
        return []

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.preorder_list_helper(self.root)

    def preorder_list_helper(self, node):
        if node is not None:
            return [node.key] + self.preorder_list_helper(node.left) + self.preorder_list_helper(node.right)
        return []

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000)  # Don't change this!
        level_order_list = []
        if not self.is_empty():
            q.enqueue(self.root)
        while not q.is_empty():
            removed = q.dequeue()
            level_order_list.append(removed.key)
            if removed.left is not None:
                q.enqueue(removed.left)
            if removed.right is not None:
                q.enqueue(removed.right)
        return level_order_list
