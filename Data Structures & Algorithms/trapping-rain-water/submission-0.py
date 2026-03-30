class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        r = len(height) - 1
        l_max = height[l]  # longest boundry from left
        r_max = height[r]  # longest boundry from right

        while l < r:
            # the shorter boundry is limiting factor, so we calculate the water for that side
            # if l_max is shorter, we calculate water using l_index
            if l_max <= r_max:
                water += l_max - height[l]
                l += 1
                l_max = max(
                    l_max, height[l]
                )  # therefore, height[l] can never be greater than l_max
            else:
                water += r_max - height[r]
                r -= 1
                r_max = max(
                    r_max, height[r]
                )  # therefore, height[r] can never be greater than r_max

        return water