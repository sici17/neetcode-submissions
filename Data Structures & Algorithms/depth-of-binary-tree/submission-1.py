# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    massimo=0


    def maxDepth(self, root: Optional[TreeNode]) -> int:

        count=1
        def depth(node,count):

            if node is None:
                return

            self.massimo=max(self.massimo,count)
            depth(node.left,count+1)
            depth(node.right,count+1)

        depth(root, count)

        return self.massimo



        

            


        




        
            

            



        
            




        
        