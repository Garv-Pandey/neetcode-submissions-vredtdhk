class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_freq = defaultdict(int)

        for num in nums:
            nums_freq[num]+=1

        answer = []
        for num, freq in nums_freq.items():
            if freq>len(nums)//3:
                answer.append(num)

        return answer