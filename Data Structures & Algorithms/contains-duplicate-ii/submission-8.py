class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_nums = set()
        if k==0:
            return False

        l = 0
        for r in range (len (nums)):
            if nums[r] in window_nums:
                return True
            
            if r-l+1 > k:
                window_nums.remove(nums[l])
                l+=1

            window_nums.add(nums[r])
        return False