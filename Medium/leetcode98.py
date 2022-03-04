# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, lowerBound, upperBound):
            if not root:
                return True 
                
            if (lowerBound!= None and root.val <= lowerBound) or (upperBound != None and root.val >= upperBound):
                return False
            
            return validate(root.left, lowerBound, root.val) and validate(root.right, root.val, upperBound)
        
        
        return validate(root, None, None)