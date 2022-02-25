class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        
        temp={}
        for i in range(nums_len):
            box=target-nums[i]
            if box in temp.keys():    
                return [temp[box],i]
            else:
                temp[nums[i]]=i