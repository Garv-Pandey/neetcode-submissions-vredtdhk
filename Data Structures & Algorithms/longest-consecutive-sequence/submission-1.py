class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        hash_set = set(nums)

        for num in nums:
            if not(num-1 not in hash_set):
                continue

            seq_len = 1
            top_ele = num
            while (top_ele+1 in hash_set):
                seq_len +=1
                top_ele +=1
                
            if (seq_len>longest_seq):
                longest_seq = seq_len

        return longest_seq
            

