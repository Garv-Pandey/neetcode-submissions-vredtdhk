class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) -1 

        while l <= r:
            while l < r and nums[l+1] == nums[l]:
                l+=1

            while l < r and nums[r] == nums[l]:
                r -= 1

            mid = l + (r-l)//2

            if nums[mid] == target:
                return True

            elif nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l = mid+1

                elif nums[mid]>target:
                    r = mid-1
            
            else:
                if nums[l] <= target or nums[mid] > target:
                    r = mid-1

                elif nums[mid]< target:
                    l = mid+1

        return False