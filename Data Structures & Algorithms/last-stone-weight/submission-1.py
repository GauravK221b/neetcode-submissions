class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            
            diff = x - y
            if diff > 0:
                stones.append(diff)
        
        if len(stones) > 0:
            return stones[0]
        else:
            return 0

            