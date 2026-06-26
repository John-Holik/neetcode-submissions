class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        
        while left < right:
            height = min(heights[left], heights[right])
            width =  right - left
            area = height * width
            if area > maxArea:
                maxArea = area
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxArea