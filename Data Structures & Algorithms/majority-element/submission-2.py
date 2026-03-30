class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        major_ele = nums[0]

        for num in nums:
            if num == major_ele:
                freq+=1
            else:
                freq-=1

            if freq < 0:
                major_ele = num
                freq = 1

        return major_ele