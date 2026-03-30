class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        result = float('inf')
        while l <= r:
            print(l,r)
            mid = l + (r - l)//2
            if nums[l] > nums[r]:
                if nums[l] <= nums[mid]:
                    l = mid+1
                # else nums[l] > nums[mid]:
                else:
                    result = min(result, nums[mid])
                    r = mid-1

            # elif nums[l] < nums[r]:
            else:
                result = min(result, nums[mid])
                r = mid-1

        return result