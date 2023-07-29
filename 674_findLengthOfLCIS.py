class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        longest = 0
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += 1
            else:
                temp = 1
           
            if temp > longest:
                longest = temp
        
        return longest
