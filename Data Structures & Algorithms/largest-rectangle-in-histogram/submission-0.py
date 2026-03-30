class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # contains subarrays [index, height at that index]

        # we keep those heights in stack which we can extend from their starting index till index i (hence the end of list when for loop ends)
        # we calculate area of every height being popped
        for i in range(len(heights)):
            start_index = i
            if len(stack) == 0:
                stack.append([start_index, heights[i]])

            while (
                len(stack) > 0 and heights[i] < stack[-1][1]
            ):  # height's area cannot be continued further
                pop_height_index, pop_height = stack.pop()
                area = pop_height * (i - pop_height_index)
                if area > max_area:
                    max_area = area

                start_index = pop_height_index  # if previous heights are longer, then the current height's area can be extended back

            # when current height is >= height on top of stack
            stack.append([start_index, heights[i]])

        print(stack)

        # area of the elements remaining in stack extend till the end of list. calculating their area now
        for start_index, height in stack:
            area = (len(heights) - start_index) * height
            if area > max_area:
                max_area = area

        return max_area