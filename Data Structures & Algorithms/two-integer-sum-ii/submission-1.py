class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_index = 0
        r_index = len(numbers)-1

        while numbers[l_index] + numbers[r_index] != target:
            if numbers[l_index] + numbers[r_index] > target:
                r_index -= 1

            if numbers[l_index] + numbers[r_index] < target:
                l_index += 1

        return [l_index+1, r_index+1]