class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = [0]*(len(nums)*2)

        for i in range(len(nums)):
            answer[i] = answer[i+len(nums)] = nums[i]

        return answer