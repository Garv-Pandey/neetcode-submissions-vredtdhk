class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = defaultdict(int)

        for num in nums:
            dict_nums[num] += 1

        bucket = [[] for i in range(len(nums)+1)]

        for num, freq in dict_nums.items():
            bucket[freq].append(num)

        result = []
        for j in range(len(bucket)-1, -1, -1):
            for num in bucket[j]:
                result.append(num)
                if len(result)==k:
                    return result
