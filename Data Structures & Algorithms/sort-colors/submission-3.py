class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0]*3

        for num in nums :
            buckets[num] += 1

        nums_point = 0
        for i in range(3):
            for j in range(buckets[i]):
                nums[nums_point] = i
                nums_point += 1


            
