class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        lMaxHeight = 0
        rMaxHeight = 0

        l_pointer = 0
        r_pointer = len(height)-1

        while l_pointer < r_pointer:

            lMaxHeight = max(lMaxHeight, height[l_pointer])
            rMaxHeight = max(rMaxHeight, height[r_pointer])

            if height[l_pointer] < height[r_pointer]:
                l_pointer += 1
                if lMaxHeight > height[l_pointer]:
                    result += lMaxHeight - height[l_pointer]

            else:
                r_pointer -=1
                if rMaxHeight > height[r_pointer]:
                    result += rMaxHeight - height[r_pointer]

        return result