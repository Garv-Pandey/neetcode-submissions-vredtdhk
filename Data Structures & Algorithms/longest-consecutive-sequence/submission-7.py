class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0

        setNums = set(nums)

        for num in nums:

            if num-1 in setNums:
                continue 

            length = 1
            target = num+1
            while target in setNums:
                length +=1
                target +=1

            result = max(result, length)

        return result