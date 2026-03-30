class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        answer = 0

        for num in nums:
            if num-1 in nums_set:
                continue

            length = 1
            while num+length in nums_set:
                length+=1

            answer = max(answer, length)

        return answer