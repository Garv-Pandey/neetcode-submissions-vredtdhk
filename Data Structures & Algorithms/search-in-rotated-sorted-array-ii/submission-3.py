class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) -1

        while l < r and nums[l] == nums[l+1]:
            l += 1

        while r > l and nums[r] == nums[l]:
            r -= 1

        while l<=r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return True
            
            elif nums[l] > nums[r]:
                if nums[mid] >= nums[l]:
                    if target >= nums[l] and target < nums[mid]:
                        r = mid -1

                    else:
                        l = mid +1

                else:
                    if target < nums[l] and target > nums[mid]:
                        l = mid+1
                    else:
                        r = mid-1

            else: 
                if target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1

        return False