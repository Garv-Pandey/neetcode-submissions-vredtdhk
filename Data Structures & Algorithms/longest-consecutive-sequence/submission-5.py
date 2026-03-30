class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        
        for num in nums:
            if num-1 in nums_set:
                continue

            target = num + 1
            seq_len = 1
            while target in nums_set:
                target+=1
                seq_len+=1

            max_len = max(max_len, seq_len)

        return max_len
