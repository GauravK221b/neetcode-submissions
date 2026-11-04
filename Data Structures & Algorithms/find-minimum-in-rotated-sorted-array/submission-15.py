class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        small = nums[0]
        while l < r:
            if nums[l] < nums[r]:
                small = nums[l]
                r -= 1
            else:
                small = nums[r]
                l += 1
        return small
