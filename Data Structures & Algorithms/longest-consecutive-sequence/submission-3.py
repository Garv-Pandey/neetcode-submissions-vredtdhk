class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_len = 0
        set_nums = set(nums)
        for num in nums:
            if num-1 in set_nums:
                continue
                # num is not a starting of sequence

            current_len = 1
            target = num + 1
            while target in set_nums:
                current_len +=1
                target +=1

            seq_len = max(seq_len, current_len)

        return seq_len

