class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        lMax = height[0]
        rMax = height[len(height)-1]

        l = 0
        r = len(height)-1

        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])

            if lMax <= rMax:
                water += lMax - height[l]
                l+=1

            else:
                water += rMax - height[r]
                r-=1
        
        return water