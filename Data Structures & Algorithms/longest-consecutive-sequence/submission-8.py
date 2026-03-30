class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_seq = 0 
        for i in range (len (nums)):
            # finding the starting number of sequence
            if nums[i]-1 in nums_set:
                continue

            seq_len = 1
            while nums[i] + seq_len in nums_set:
                seq_len+=1

            longest_seq = max(longest_seq, seq_len)

        return longest_seq