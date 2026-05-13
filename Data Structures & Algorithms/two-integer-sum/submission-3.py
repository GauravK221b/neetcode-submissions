class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_hash = {}
        solution = []

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in pre_hash:
                solution.append(pre_hash[diff])
                solution.append(i)
                return solution

            else:
                pre_hash[n] = i