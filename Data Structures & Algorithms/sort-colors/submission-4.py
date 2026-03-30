class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0]*3

        for num in nums:
            buckets[num] += 1

        nums_point = 0
        for i in range(len(buckets)):
            for _ in range(buckets[i]):
                nums[nums_point] = i
                nums_point+=1