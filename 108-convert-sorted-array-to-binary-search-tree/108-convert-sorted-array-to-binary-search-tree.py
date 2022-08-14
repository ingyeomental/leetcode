# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        
        middle_idx = len(nums)//2
        middle_num = nums[middle_idx]
        
        node = TreeNode(val = middle_num)
        
        node.left = self.sortedArrayToBST(nums = nums[0:middle_idx])
        node.right = self.sortedArrayToBST(nums = nums[middle_idx+1:])
        
        return node
        
        