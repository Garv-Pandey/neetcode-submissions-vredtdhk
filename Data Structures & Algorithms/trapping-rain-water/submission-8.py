class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 #index
        r = len(height) - 1

        l_max = height[l] #height
        r_max = height[r]

        area = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            
            if l_max <= r_max:
                area+= l_max - height[l]
                l+=1

            else:
                area+= r_max - height[r]
                r-=1

        return area
