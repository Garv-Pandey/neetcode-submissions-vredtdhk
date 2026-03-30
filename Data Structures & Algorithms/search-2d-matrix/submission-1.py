class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        l = 0
        r = rows -1 
        target_row = rows - 1
        while l<=r:
            cur_row = l+(r-l)//2

            if matrix[cur_row][-1] < target:
                l = cur_row+1

            elif matrix[cur_row][-1] > target:
                target_row = min(cur_row, target_row)
                r = cur_row-1
            
            else:
                target_row = cur_row
                break
        
        l_row = 0
        r_row = columns-1
        while l_row <= r_row:
            ele_index = l_row + (r_row - l_row)//2

            if matrix[target_row][ele_index] == target:
                return True
            
            elif matrix[target_row][ele_index] < target:
                l_row = ele_index +1

            else:
                r_row = ele_index-1

        return False
        