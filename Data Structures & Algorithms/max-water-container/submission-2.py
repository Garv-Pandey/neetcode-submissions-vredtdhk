class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        l_point = 0
        r_point = len(heights)-1

        while l_point < r_point:

            vol = min(heights[l_point], heights[r_point]) * (r_point-l_point)

            result = max(result, vol)

            if heights[l_point] <= heights[r_point] and l_point < r_point:
                l_point += 1

            elif heights[l_point] > heights[r_point] and l_point < r_point:
                r_point -= 1

        return result
