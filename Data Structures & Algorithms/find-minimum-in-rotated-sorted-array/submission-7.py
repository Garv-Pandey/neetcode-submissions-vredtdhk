class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        answer = float('inf')
        while l <= r:
            mid = l + (r-l)//2

            if nums[l] > nums[r]:
                if nums[mid] >= nums[l]:
                    l = mid+1

                else:
                    answer = min(answer, nums[mid])
                    r = mid-1
            else:
                answer = min(answer, nums[l])
                break

        return answer