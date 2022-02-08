# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return True if self.height(root) != -1 else False
    
    def height(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1