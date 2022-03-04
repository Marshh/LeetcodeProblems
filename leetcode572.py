# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(r,s):
            if(r == None or s == None):
                return r == None and s == None
            elif(r.val == s.val):
                return isSameTree(r.left, s.left) and isSameTree(r.right, s.right)
            else:
                return False
            
            
        if(root == None):
            return False
        elif(isSameTree(root,subRoot)):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
             
            