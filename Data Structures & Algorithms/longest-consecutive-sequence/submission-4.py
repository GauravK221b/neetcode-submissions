class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        longest = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - nums[i -1] == 1:
                count += 1
            else:
                count = 1
            
            longest = max(count , longest)
        
        return longest
