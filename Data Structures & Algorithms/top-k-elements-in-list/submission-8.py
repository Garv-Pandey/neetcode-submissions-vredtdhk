class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = dict()

        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1

        buckets = [[] for i in range(len(nums)+1)]

        for num, freq in nums_map.items():
            buckets[freq].append(num)

        answer = []
        for j in range(len(buckets)-1, -1, -1):
            for num in buckets[j]:
                answer.append(num)
                if len(answer) == k:
                    return answer
                
        return answer