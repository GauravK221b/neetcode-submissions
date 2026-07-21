class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, num in enumerate(nums):
            res[num] = i
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in res and res[diff] != i:
                return[i, res[diff]]
        return []
                