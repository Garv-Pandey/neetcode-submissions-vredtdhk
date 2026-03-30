class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_stack = [] #stores indices/days whole larger temp is not found
        answer = [0]*len(temperatures)
        for i in range (len (temperatures)):
            if not index_stack:
                index_stack.append(i)
                continue

            while index_stack and temperatures[i] > temperatures[index_stack[-1]]:
                answer[index_stack[-1]] = i - index_stack[-1]
                index_stack.pop()

            index_stack.append(i)

        return answer

            