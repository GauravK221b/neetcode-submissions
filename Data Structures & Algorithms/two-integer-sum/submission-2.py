class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_hash = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in pre_hash:
                return [pre_hash[diff],i]
            pre_hash[n] = i
        return