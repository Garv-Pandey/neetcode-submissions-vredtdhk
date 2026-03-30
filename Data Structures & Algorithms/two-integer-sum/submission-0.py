class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = dict()
        for i in range (0, len(nums)):
            value_find = target-nums[i]
            
            if (value_find in hash_map):
                return [hash_map[value_find], i]

            hash_map[nums[i]]= i