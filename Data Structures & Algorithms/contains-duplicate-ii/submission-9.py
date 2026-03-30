class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        l = 0
        for i in range(len(nums)):
            if nums[i] in window_set:
                return True
            
            window_set.add(nums[i])
            if i-l+1 > k:
                window_set.remove(nums[l])
                l+=1

        return False