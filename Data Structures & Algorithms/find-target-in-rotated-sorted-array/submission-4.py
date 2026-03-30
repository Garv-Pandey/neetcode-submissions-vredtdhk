class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # finding which part of the array we are in
            if nums[l] > nums[r]:
                if nums[mid] >= nums[l]:
                    # mid is in left part
                    if nums[l] <= target < nums[mid]:
                        r = mid - 1

                    else:
                        l = mid + 1

                else:
                    # mid is in right part
                    if nums[mid] < target <= nums[r]:
                        l = mid + 1

                    else:
                        r = mid - 1

            else:
                # simple sorted array selected between l and r
                if nums[mid] < target:
                    l = mid + 1

                else:
                    r = mid - 1

        return -1
