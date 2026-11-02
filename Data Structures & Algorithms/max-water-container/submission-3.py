class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        curr_area = 0
        while l < r:
            le = r - l
            height = min(heights[l], heights[r])
            curr_area = max(curr_area, le * height)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return curr_area
