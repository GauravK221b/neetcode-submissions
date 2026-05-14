class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)

        sorted_item = sorted(count, key = count.get, reverse = True)

        return sorted_item[:k]
        