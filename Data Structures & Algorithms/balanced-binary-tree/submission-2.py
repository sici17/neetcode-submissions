# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    flag=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(node):

            if node is None:
                return 0

            leftheight=balance(node.left)
            rightheight=balance(node.right)
            if abs(leftheight-rightheight)>1:
                self.flag=False

            return max(leftheight,rightheight) + 1

        balance(root)
        if self.flag:
            return True
        else:
            return False



        


        