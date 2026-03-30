class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []
        for i in range(0, len(nums) - 2):  # -2 to make space for index j and k
            if nums[i] > 0:
                break

            if nums[i] == nums[i - 1] and i != 0:
                continue

            j = i + 1  # left index for two point squeeze
            k = len(nums) - 1  # right index for two point squeeze
            while j < k:
                if nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                    continue

                if nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                    continue

                triplets.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while nums[j - 1] == nums[j] and j<k:
                    j += 1
                # we dont need to skip same number for k (will be handled by if statements above) because
                # i stays same, we are getting different j.
                # then our condition of getting the sum 0 will never fullfill until k changes to a different number
                # changes in atleast two numbers are required to get same result.
                # We are changing one number, other number will be changed autommaticlly trying to find combination that fullfills our condition

        return triplets
