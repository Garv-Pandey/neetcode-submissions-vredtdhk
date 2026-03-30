class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range (len(heights)):
            if not stack or stack[-1][1] < heights[i]:
                stack.append((i, heights[i]))
                continue

            if heights[i]==heights[i-1]:
                continue

            index, height = 0, 0
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                print(i, index, height)
                area = (i-index)*height
                maxArea = max(maxArea, area)


            stack.append((index, heights[i]))

        # emptying the stack
        print(stack)
        for j in range(len(stack)):
            index, height = stack[j] 
            area = (len(heights) - index)*height
            maxArea = max(maxArea, area)

        return maxArea

            