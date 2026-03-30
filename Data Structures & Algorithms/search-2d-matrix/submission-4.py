class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL = 0
        rowR = len(matrix) -1
        target_row = rowR
        while rowL <= rowR:
            mid = rowL + (rowR - rowL)//2

            if matrix[mid][-1] < target:
                rowL = mid + 1

            else:
                target_row = min(target_row, mid)
                rowR = mid -1

        l = 0
        r = len(matrix[0]) -1
        print(target_row)
        while l <= r:
            mid = l + (r-l)//2

            if matrix[target_row][mid] == target:
                return True
            
            elif matrix[target_row][mid] > target:
                r = mid-1

            else:
                l = mid+1

        return False