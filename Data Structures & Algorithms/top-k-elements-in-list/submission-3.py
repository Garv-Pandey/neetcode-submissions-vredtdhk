class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums = {}
        for i in range(len(nums)): 
            value = map_nums.get(nums[i], 0)+1
            map_nums[nums[i]] = value

        # print (map_nums)

        buckets = [[] for i in range(len (nums) +1)]
        for key, freq in map_nums.items():
            buckets[freq].append(key)

        print (buckets)

        result = []
        for j in range(len(buckets)-1, 0, -1):
            for num in buckets[j]:
                result.append(num)

            if len(result)==k:
                return result
            

