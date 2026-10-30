# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        copied = root
        # check current node and see if > or <
        # if val is <, next node is left child
        # if val is >, next node is right child
        # before moving, if destination is a null, then create a
        # tree node and insert
        inserted = False
        if copied is None:
            root = TreeNode(val=val)
            return root
        
        while inserted == False:
            if copied.val < val:
                print(copied.val)
                if copied.right is None:
                    new = TreeNode(val=val)
                    copied.right = new
                    inserted = True
                copied = copied.right
            if copied.val > val:
                print(copied.val)
                if copied.left is None:
                    new = TreeNode(val=val)
                    copied.left = new
                    inserted = True
                copied = copied.left
        return root