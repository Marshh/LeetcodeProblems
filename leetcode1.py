class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp = dict()
        
        for i in range(0, len(nums)):
            if(nums[i] in temp):
                return([temp[nums[i]],i])
            else:
                temp[target-nums[i]] = i
                
        return [0,0]