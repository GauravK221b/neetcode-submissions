class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i , num in enumerate(nums):
            hash_map[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map and hash_map[diff] != i:
                return [i, hash_map[diff]]
        
        return []
        
