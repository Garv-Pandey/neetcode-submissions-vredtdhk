class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = list()
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append([temperatures[i], i])
                continue

            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                lower_temp_index = stack[-1][1]
                result[lower_temp_index] = i - lower_temp_index
                stack.pop()

            stack.append([temperatures[i], i])

        return result