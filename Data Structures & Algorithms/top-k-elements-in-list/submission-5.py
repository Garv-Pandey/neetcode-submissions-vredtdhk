class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        
        for num in nums:
            nums_dict[num]+=1

        print(nums_dict)

        buckets = [[] for i in range(len(nums)+1)]
        for num, freq in nums_dict.items():
            buckets[freq].append(num)

        result = []
        for i in range (len(buckets)-1, -1, -1):            
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
