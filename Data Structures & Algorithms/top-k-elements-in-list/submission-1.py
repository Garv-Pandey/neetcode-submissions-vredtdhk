class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map_freq = {}
        for num in nums:
            map_freq[num] = map_freq.get(num,0)+1

        bucket = [[] for i in range (len(nums)+1)]
      
        for ele, freq in map_freq.items():
            bucket[freq].append(ele)

        result = []
        for i in range (len(bucket)-1, 0 , -1):
            for ele in bucket[i]:
                result.append(ele)
                if len(result) == k:
                    return result