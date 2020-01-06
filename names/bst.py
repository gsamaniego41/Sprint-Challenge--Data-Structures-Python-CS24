class BinarySearchTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # insert left if value is less than node
        if value < self.value:
            # if empty, create a new tree with its own value, left, and right properties
            if not self.left:
                self.left = BinarySearchTree(value)
            # else, keep going
            else:
                # self.left has its own left and right
                self.left.insert(value)
        # insert right if value is equal or greater than node
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        # if target == self.value, return it
        # go left or right based on smaller or bigger

        # base case
        if target == self.value:
            return True

        if target < self.value:
            if not self.left:
                # no child node
                return False
            else:
                # keep searching
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        max = self.value

        while self:
            if self.value > max:
                max = self.value
            self = self.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # keep iterating as long as current node has left and right
        if not self:
            return
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        # keep iterating
        cb(self.value)
