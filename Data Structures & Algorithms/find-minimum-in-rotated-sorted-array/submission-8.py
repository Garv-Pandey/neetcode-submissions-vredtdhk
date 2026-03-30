class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = nums[0]

        while l <= r:
            mid = l + (r - l) // 2

            # finding which part of the array we are in
            if nums[l] > nums[r]:
                # rotated array selected between l and r
                if nums[mid] > nums[r]:
                    # left part of the rotated array
                    l = mid + 1

                else:
                    # right part of the rotated array
                    ans = min(ans, nums[mid])
                    r = mid - 1

            else:
                # simple sorted array selected between l and r
                ans = min(nums[l], ans)
                return ans
