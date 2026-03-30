class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        
        l_maxhi = 0
        r_maxhi = 0

        l_point = 0
        r_point = len(height)-1

        while l_point<r_point:
            l_maxhi = max(l_maxhi, height[l_point])
            r_maxhi = max(r_maxhi, height[r_point])
            
            if height[l_point] < l_maxhi:
                water += l_maxhi - height[l_point]
            
            if height[r_point] < r_maxhi:
                water += r_maxhi - height[r_point]

            if height[l_point] <= height[r_point] and l_point<r_point:
                l_point += 1
            elif height[l_point] > height[r_point] and l_point<r_point:
                r_point -=1

        return water
