class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = None

        row_l = 0
        row_r = len(matrix)-1

        while row_l<=row_r:
            mid = row_l + (row_r-row_l)//2

            if matrix[mid][0] > target:
                row_r = mid - 1

            else:
                target_row = mid
                row_l = mid+1

        if target_row == None:
            print("no target row")
            return False

        col_l = 0
        col_r = len(matrix[0])-1

        while col_l<=col_r:
            mid = col_l + (col_r - col_l)//2

            if matrix[target_row][mid] == target:
                return True
            
            elif matrix[target_row][mid] < target:
                col_l = mid+1

            else:
                col_r = mid-1

        return False