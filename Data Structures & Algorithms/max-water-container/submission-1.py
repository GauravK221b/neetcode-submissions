class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        area = 0
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            current_area = length * height
            area = max(current_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area