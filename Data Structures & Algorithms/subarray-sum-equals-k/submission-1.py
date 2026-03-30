class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result= 0
        prefixSum_count = defaultdict(int)
        
        windowSum = 0
        for i in range (len(nums)):
            windowSum += nums[i]

            # increasing the subarray count if the current arrays sum matches the desired result
            if windowSum == k:
                result+=1

            # calculating what sum of subarray of window we need to remove the get result
            remove_value = windowSum - k

            # checking how many subarray we have encountered with the desired remove_value
            if remove_value in prefixSum_count:
                result += prefixSum_count[remove_value]

            # adding the sum of current window to the dict
            prefixSum_count[windowSum] += 1

        return result