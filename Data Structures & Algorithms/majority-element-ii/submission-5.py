class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_freq = defaultdict(int)

        for i in range(len(nums)):
            # updating the number and frequency
            num_freq[nums[i]] += 1 

            # pruning the dict if required
            if len(num_freq) == 3:
                num_to_remove = []
                
                # finding keys to remove
                for num in num_freq.keys():
                    num_freq[num] -= 1
                    if num_freq[num] == 0:
                        num_to_remove.append(num)

                # removing keys
                for num in num_to_remove:
                    del num_freq[num]
                
        print(num_freq)
        # checking the possible numbers
        answer=[]
        for num in num_freq.keys():
            freq = 0
            for i in range(len(nums)):
                if nums[i] == num:
                    freq += 1
            
            if freq > len(nums)//3:
                answer.append(num)

        return answer