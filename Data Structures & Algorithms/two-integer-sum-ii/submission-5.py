class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while l<r and r<len(numbers):
            total = numbers[l] + numbers[r]

            if l!=r and total==target:
                return[l+1,r+1]
            
            if total > target:
                r-=1

            elif total<target:
                l+=1

        