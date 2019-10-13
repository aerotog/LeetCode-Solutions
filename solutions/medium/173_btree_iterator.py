# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root

        self.ordered_vals = []

        self.index = 0

        self.process(root)

    def process(self, node: TreeNode):
        if (node is None):
            return

        self.process(node.left)
        self.ordered_vals.append(node.val)
        self.process(node.right)

    def next(self) -> int:
        num = self.ordered_vals[self.index]
        self.index += 1
        return num
        """
        @return the next smallest number
        """

    def hasNext(self) -> bool:
        return self.index < len(self.ordered_vals)
        """
        @return whether we have a next smallest number
        """

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()