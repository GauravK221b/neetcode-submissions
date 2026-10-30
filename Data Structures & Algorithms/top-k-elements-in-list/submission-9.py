class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        return sorted(freq, key = freq.get, reverse= True)[:k]