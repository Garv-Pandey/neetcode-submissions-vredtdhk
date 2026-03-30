class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)

        for num in nums:
            nums_freq[num]+=1

        buckets = [[] for i in range (len(nums) + 1)]
        for num, freq in nums_freq.items():
            buckets[freq].append(num)

        print(buckets)

        answer = []
        for j in range(len(buckets) -1, -1, -1):
            for num in buckets[j]:
                answer.append(num)
                if len(answer) == k:
                    return answer

        return answer

