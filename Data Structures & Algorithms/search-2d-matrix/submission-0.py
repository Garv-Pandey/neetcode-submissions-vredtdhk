class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        top = 0
        bottom = len(matrix)-1

        while top<=bottom:
            mid_row = top + (bottom-top)//2

            if matrix[mid_row][0] >target:
                bottom = mid_row - 1

            elif matrix[mid_row][-1] < target:
                top = mid_row +1

            else:
                break

        if not top <= bottom:
            return False
        
        row = top + (bottom-top)//2
        l = 0
        r = C-1

        while l<=r:
            mid = l + (r-l)//2

            if matrix[row][mid] > target:
                r = mid-1

            elif matrix[row][mid] < target:
                l = mid +1

            else:
                return True
            
        return False