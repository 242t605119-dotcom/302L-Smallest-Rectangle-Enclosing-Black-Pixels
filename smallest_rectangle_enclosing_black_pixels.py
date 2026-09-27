class Solution:
    def minArea(self, image, x, y):
        rows = len(image)
        cols = len(image[0])

        min_row = rows
        max_row = -1
        min_col = cols
        max_col = -1

        for i in range(rows):
            for j in range(cols):
                if image[i][j] == '1':
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        return (max_row - min_row + 1) * (max_col - min_col + 1)
