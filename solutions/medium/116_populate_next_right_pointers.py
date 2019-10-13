# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root.left is not None:
            root.left.next = root.right
            self.connect(root.left)

        if root.right is not None:
            if root.next is not None:
                root.right.next = root.next.left
            self.connect(root.right)

        return root


n7 = Node(7)
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n6, n7)
n2 = Node(2, n4, n5)
root_node = Node(1, n2, n3)

sol = Solution()
solved_node = sol.connect(root_node)

print("DONE")
