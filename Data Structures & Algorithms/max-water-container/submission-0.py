class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l_point = 0
        r_point = len(heights)-1
        while l_point < r_point:
            water = min(heights[l_point],heights[r_point]) * (r_point - l_point)

            if (water > max_water):
                max_water = water

            if heights[l_point] < heights[r_point]:
                l_point += 1
            else:
                r_point -=1

        return max_water