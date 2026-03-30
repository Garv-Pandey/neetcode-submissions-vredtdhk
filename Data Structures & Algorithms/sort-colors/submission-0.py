class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0]*3

        for num in nums:
            bucket[num] += 1

        num_pointer = 0
        for i in range(len(bucket)):
            for j in range (bucket[i]):
                nums[num_pointer] = i
                num_pointer+=1