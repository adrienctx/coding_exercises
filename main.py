# -*- coding: utf-8 -*-
from largest_rectangle import *
from stock_trade import *
from CL_index import *


def main():
    """
    Here are some simple test cases to experiment with the scripts
    """
    matrix = [[0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 1], [1, 1, 1, 0, ], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]]
    max_area, start_row_idx, start_col_idx, length, height = max_ones_rectangle_area(matrix)
    print('matrix is ')
    print(matrix)
    print('max area, row_idx, col_idx, l, h, are : %d, %d, %d, %d, %d' % (
        max_area, start_row_idx, start_col_idx, length, height))

    stock_prices = [5, 6, 4, 7, 9, 8, 8]
    my_tuple = find_best_trade(stock_prices)
    print('best trade is : buy at index %d, sell at index %d, profit is %d', my_tuple[1], my_tuple[2], my_tuple[0])

    text = "Existing computer programs that measure readability are based largely upon subroutines which estimate number of syllables, usually by counting vowels. The shortcoming in estimating syllables is that it necessitates keypunching the prose into the computer. There is no need to estimate syllables since word length in letters is a better predictor of readability than word length in syllables. Therefore, a new readability formula was computed that has for its predictors letters per 100 words and sentences per 100 words. Both predictors can be counted by an optical scanning device, and thus the formula makes it economically feasible for an organization such as the U.S. Office of Education to calibrate the readability of all textbooks for the public school system."
    print("CLI of text 1 is %f" % get_coleman_liau_idx(text))

    text2 = "The best things in an artist’s work are so much a matter of intuition, that there is much to be said for the point of view that would altogether discourage intellectual inquiry into artistic phenomena on the part of the artist. Intuitions are shy things and apt to disappear if looked into too closely. And there is undoubtedly a danger that too much knowledge and training may supplant the natural intuitive feeling of a student, leaving only a cold knowledge of the means of expression in its place. For the artist, if he has the right stuff in him ... "
    print("CLI of text 2 is %f" % get_coleman_liau_idx(text2))
    return 0


if __name__ == "__main__":
    main()
