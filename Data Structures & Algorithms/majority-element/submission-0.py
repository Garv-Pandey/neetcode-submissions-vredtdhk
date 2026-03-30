class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        max_num, max_freq = 0,0
        for num in nums:
            freq[num]+=1
            if freq[num]>max_freq:
                max_freq = freq[num]
                max_num = num

        return max_num
