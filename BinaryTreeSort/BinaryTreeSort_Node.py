class BinaryTreeSort_Node:
    def __init__(self, val=None):
        self.val = val
        self.left_tree = None
        self.right_tree = None

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left_tree:
                self.left_tree.insert(val)
                return
            self.left_tree = BinaryTreeSort_Node(val)
            return

        if self.right_tree:
            self.right_tree.insert(val)
            return
        self.right_tree = BinaryTreeSort_Node(val)

    def get_min(self):
        current = self
        while current.left_tree is not None:
            current = current.left_tree
        return current.val

    def get_max(self):
        current = self
        while current.right_tree is not None:
            current = current.right_tree
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left_tree:
                self.left_tree = self.left_tree.delete(val)
            return self
        if val > self.val:
            if self.right_tree:
                self.right_tree = self.right_tree.delete(val)
                return self
            if self.right_tree is None:
                return self.left_tree
            if self.left_tree is None:
                return self.right_tree
            min_larger_node = self.right_tree
            while min_larger_node.left_tree:
                min_larger_node = min_larger_node.left_tree
            self.val = min_larger_node.val
            self.right_tree = self.right_tree.delete(min_larger_node.val)
            return self

    def exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left_tree is None:
                return False
            return self.left_tree.exists(val)
        if self.right_tree is None:
            return False
        return self.right_tree.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left_tree is not None:
            self.left_tree.preorder(vals)
        if self.right_tree is not None:
            self.right_tree.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left_tree is not None:
            self.left_tree.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right_tree is not None:
            self.right_tree.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left_tree is not None:
            self.left_tree.postorder(vals)
        if self.right_tree is not None:
            self.right_tree.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals






