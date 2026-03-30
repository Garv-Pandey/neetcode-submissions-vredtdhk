class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax = height[r]
        while l<r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])

            if lMax<=rMax:
                water+= lMax-height[l]
                l+=1
            else:
                water+= rMax-height[r]
                r-=1

        return water