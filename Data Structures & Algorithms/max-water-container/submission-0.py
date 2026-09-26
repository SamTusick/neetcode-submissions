class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            water = width * height

            if water > max_water:
                max_water = water
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1  # covers both < and if they equal
        return max_water