# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
      
    massimo=0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        def diameter(node):

            if node is None:
                return 0

            leftheight=diameter(node.left)
            rightheight=diameter(node.right)
            self.massimo=max(self.massimo, leftheight+rightheight)

            return max(leftheight,rightheight) + 1

        diameter(root)
        return self.massimo

        
        


        
        