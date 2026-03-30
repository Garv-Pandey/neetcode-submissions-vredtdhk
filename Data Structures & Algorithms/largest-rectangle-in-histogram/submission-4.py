class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        answer = 0
        for i in range(len(heights)):

            if not stack or heights[i] > stack[-1][0]:
                stack.append((heights[i], i))
                continue
            
            if heights[i] == stack[-1][0]:
                continue

            height = index  = 0
            while stack and heights[i] < stack[-1][0]:
                height, index = stack[-1]
                area = height * (i - index)
                answer = max (answer, area)
                stack.pop()

            stack.append((heights[i], index))

        for h in stack:
            height , index = h
            print(height, index)
            area = (len(heights) - index) * height
            answer = max(answer, area)

        return answer