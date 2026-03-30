class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # finding the column
        col_l = 0
        col_r = len(matrix) - 1
        target_col = None

        while col_l <= col_r:
            col_mid = col_l + (col_r - col_l) // 2

            if matrix[col_mid][0] <= target <= matrix[col_mid][-1]:
                target_col = col_mid
                break

            elif matrix[col_mid][-1] < target:
                col_l = col_mid + 1

            else:
                col_r = col_mid - 1

        if target_col is None:
            return False

        # finding target value
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[target_col][mid] == target:
                return True

            elif matrix[target_col][mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False
