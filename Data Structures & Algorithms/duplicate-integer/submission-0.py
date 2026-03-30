class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        temp_set = set()
        for i in nums:
            if i in temp_set:
                return True
            temp_set.add(i)
        
        return False