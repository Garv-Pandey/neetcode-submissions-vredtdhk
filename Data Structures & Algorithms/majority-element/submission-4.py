class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = 1
        majority_ele = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == majority_ele:
                majority_count += 1
                continue
            else:
                majority_count -= 1
                if majority_count == 0:
                    majority_count = 1
                    majority_ele = nums[i]
                continue

        return majority_ele
