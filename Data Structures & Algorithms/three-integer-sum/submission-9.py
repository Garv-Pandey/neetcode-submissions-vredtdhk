class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        for i in range (len(nums)-2):
            if i>0 and nums[i-1] == nums[i]:
                continue

            l_point = i+1
            r_point = len(nums)-1  

            while l_point<r_point:
                if nums[i] + nums[l_point] + nums[r_point] == 0:
                    result.append([nums[i] , nums[l_point] , nums[r_point]])  

                    l_point+=1
                    while nums[l_point] == nums[l_point-1] and l_point<r_point:
                        l_point+=1

                elif nums[i] + nums[l_point] + nums[r_point] < 0:
                    l_point +=1

                elif nums[i] + nums[l_point] + nums[r_point] > 0:
                    r_point -=1

        return result