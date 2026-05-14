class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prehash = {}
        solution = []

        for i, n in enumerate(nums):
            compliment = target - nums[i]
            if compliment in prehash:
                solution.append(prehash[compliment])
                solution.append(i)
                return solution
            else:
                prehash[n] = i