class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Basically we are doing a binary search to find the row first which row to iterate
        top, bot = 0, ROWS-1
        while top <= bot:
            midRow = (top+bot) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow -1
            else:
                break
        
        if not top <= bot:
            return False
        
        # based on the top and bot value we compute the mid row
        row = (top + bot) // 2
        l, r = 0, COLS-1
        while l <= r:
            # based on that row we compute the mid index of that row and perform binary search again
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False

