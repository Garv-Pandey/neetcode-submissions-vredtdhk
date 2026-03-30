class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_point = 0
        r_point = len(numbers)-1

        while numbers[l_point] + numbers[r_point] != target:
            if numbers[l_point] + numbers[r_point] > target:
                r_point-=1
                continue

            if numbers[l_point] + numbers[r_point] < target:
                l_point+=1
                continue

        return [l_point+1, r_point+1]