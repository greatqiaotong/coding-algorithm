# 04 - Search a 2D matrix ([leetcode 240](https://leetcode.com/problems/search-a-2d-matrix-ii/))

## Question
> Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
> * Integers in each row are sorted in ascending from left to right.
> * Integers in each column are sorted in ascending from top to bottom.

### Solution
Start the search from top-right corner or bottom-left corner so that the search range in the matrix can be reduced each time until we find the target, or until the search range becomes None.

Time complexity is <em>O</em>(<em>m</em>+<em>n</em>) where (<em>m</em>,<em>n</em>) is the size of the matrix. Space complexity is <em>O</em>(1).
```Python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if len(matrix) == 0:
        raise ValueError("Matrix is empty.")
    else:
        found = False
        rows, columns = len(matrix), len(matrix[0])
        # Search from top-right corner
        row, col = 0, columns - 1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                found = True
                break
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
    return found
```
