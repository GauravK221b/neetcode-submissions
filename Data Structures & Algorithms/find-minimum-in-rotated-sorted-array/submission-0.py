class Solution:
    def findMin(self, nums: List[int]) -> int:
        minN = nums[0]
        for i in range(len(nums)):
            minN = min(nums[i],minN)
        return minN