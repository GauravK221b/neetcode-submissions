class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while (l < r):
            leng = r - l
            h = min(heights[l],heights[r])
            curr_area = leng * h
            area = max(curr_area , area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return area
