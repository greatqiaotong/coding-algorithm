def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Find out whether a target is in the provided matrix.

    :param list[list[int]] matrix: a 2d matrix where integers in each row are sorted in ascending from left to right,
                                   and integers in each column are sorted in ascending from top to bottom
    :param int target: the target number
    :raises ValueError: matrix is empty
    :return bool: True when target in matrix and False when not in
    """
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
