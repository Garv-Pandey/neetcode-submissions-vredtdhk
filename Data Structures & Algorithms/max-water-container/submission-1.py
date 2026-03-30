class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_point = 0
        r_point = len(heights) -1
        result = 0
        
        while l_point < r_point:
            vol = min(heights[l_point], heights[r_point])*(r_point - l_point)
            result = max(vol, result)
            print(l_point, r_point, vol)

            if (heights[l_point]<heights[r_point]):
                l_point+=1
            else:
                r_point-=1

        return result

