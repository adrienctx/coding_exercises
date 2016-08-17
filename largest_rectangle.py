"""
Question:
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
And what are the time complexity and space complexity of your answer?

Our approach:
1. For each row i, for each column j, we compute (and update) heights[j], the number of consecutive 1's above matrix[i][j]
(i.e. in the column j, starting from row i (including i) and going upwards)
2. for each row i, we compute the maximum area rectangle that has its lower side contained in row i, using the
height array heights[:] ; it is equivalent to looking for the largest rectangle that fits under the "curve" of the
height array
3. the maximum area rectangle is the maximum area computed in step 2

1. takes about O(n) space and time (with n matrix cells)
2. is done once per row, and takes O(n) space and time
3. is done in O(n_rows), so O(n)
"""


def max_ones_rectangle_area(matrix):
    """
    Main function, that finds the largest rectangle with all 1's in a given matrix.

    Args:
        matrix (2D array): the given matrix
    Returns:
        max_area (int): the area of the largest rectangle
        start_row_index (int): the row index of the lower left corner of that rectangle
        start_col_index (int): the column index of that corner
        width (int): the width of that rectangle
        height (int): its height
    """

    n_rows = len(matrix)

    if n_rows == 0:
        return 0, 0, 0, 0, 0
    n_cols = len(matrix[0])
    # heights is a 1d array, of length equal to a row of matrix
    # we want to iterate from the top row to the bottom row of matrix so that when visiting a row i, for all columns j,
    # heights[j] contains the number of consecutive 1's above (and including) matrix[i][j]
    heights = [0] * n_cols

    # initializing the first row of 2D array heights
    for j in range(n_cols):
        heights[j] = matrix[0][j]
    # initializing the returned values (i.e. "rectangles" with all 1's that fit in the top row)
    max_area, max_area_start_col_index, max_area_width, max_area_height = get_largest_rect_under_curve(heights)
    max_area_start_row_idx = 0

    # for each row after the first one (if any), the heights are incremented by 1 if we find a 1, reset to 0 otherwise
    for i in range(1, n_rows):
        for j in range(n_cols):
            if matrix[i][j] == 0:
                heights[j] = 0
            else:
                heights[j] += 1
        # update the max area by comparing it to the one that can be found from the current row
        area, start_col_idx, width, height = get_largest_rect_under_curve(heights)
        # if the newly found area is larger than the largest found before, update the result
        if area > max_area:
            max_area = area
            max_area_start_row_idx = i
            max_area_width = width
            max_area_height = height
            max_area_start_col_index = start_col_idx

    return max_area, max_area_start_row_idx, max_area_start_col_index, max_area_width, max_area_height


def get_largest_rect_under_curve(heights_row):
    """
    Returns the maximum area of a rectangle that fits under the "curve" of the heights_row array

    Args:
        heights_row (1D array of ints): an array of ints; each element heights_row[i] represents the height of the curve
        under which we try to fit a rectangle.

    Returns:
        max_area (int): the area of the largest rectangle that fits under the given curve
        start_idx (int): the index of the lower left corner of that rectangle
        width (int): the width of that rectangle
        height (int): the height of that rectangle

    Method:

    We start with the first element of the heights_row array, and iterate through the array, from left to right.
    Let us call i the index where we are pointing in this array.
    We call "alive rectangle" a rectangle that, given i, has its lower left index in column j<i,
    and has a height heights_row[j].
    In other words, it's a rectangle that started in column j, before i,
    and at its highest possible height to fit under the curve.

    We maintain a list of such rectangles as i goes from 0 to len(heights_row),
    and call it alive_rectangles_starting_indexes.
    This list is naturally sorted in a LIFO way, so that the last element in it is the highest alive rectangle
    (but not necessarily the largest in area!).

    Consequence: when visiting element i in heights_row array, we only start a new alive rectangle if its height is
    larger than all alive rectangles. If the height in i is lower than some alive rectangles,
    we "kill" them: they cannot grow wider, so we compute their area, and remove them from the list.

    This way we only visit each cell once, and maintain a small structure in memory to keep track of valid rectangles.
    """

    # alive_rect_idx = [] is an array, acting as a pile (LIFO); it contains the INDEXES where alive rectangles started
    # (their column index; the row index is fixed in this sub-function).
    # The last element of this array is the starting index of the "youngest" alive rectangle (so, also the tallest).
    alive_rect_idx = []
    max_area = 0
    max_area_start_index = 0
    #   Adding some informative variables, in case we decide later we also want to know where is the largest rectangle
    max_area_width = 0
    max_area_height = 0

    for i in range(len(heights_row)):
        if len(alive_rect_idx) == 0:  # if there are no alive rectangles, any non 0 height starts a rectangle
            if heights_row[i] > 0:
                alive_rect_idx.append(i)
        else:   # there are some alive rectangles, sorted by increasing height
            # kill all rectangles that have a bigger height than the currently visited one
            while len(alive_rect_idx) > 0 and heights_row[i] < heights_row[alive_rect_idx[-1]]:
                # first, measure the area of the rectangle we're about to "kill"
                width = i - alive_rect_idx[-1]
                height = heights_row[alive_rect_idx[-1]]
                area = width * height
                # then actually remove it from the pile
                start_idx = alive_rect_idx.pop()
                # and check if it's the new largest area
                if area > max_area:
                    max_area = area
                    max_area_start_index = start_idx
                    max_area_width = width
                    max_area_height = height

            # now, check if we should start a new alive rectangle
            if len(alive_rect_idx)==0 or heights_row[i] > heights_row[alive_rect_idx[-1]]:
                alive_rect_idx.append(i)
    return max_area, max_area_start_index, max_area_width, max_area_height
