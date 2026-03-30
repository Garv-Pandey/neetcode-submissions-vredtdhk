class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        result = 0

        for num in nums:
            if num-1 in set_nums:
                continue

            target = num+1
            length = 1
            while target in set_nums:
                target += 1
                length += 1

            result= max(result, length)

        return result