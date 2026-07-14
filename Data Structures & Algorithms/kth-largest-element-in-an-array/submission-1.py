class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        ite = 1
        while ite < k :
            heapq.heappop(maxHeap)
            ite += 1
        
        return -maxHeap[0]
        