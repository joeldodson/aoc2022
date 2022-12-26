#!/usr/bin/env python

""" aoc2022/day08/part1.py 

https://adventofcode.com/2022/day/8

--- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.
First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.
The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:
30373
25512
65332
33549
35390
Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:
  - The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
  - The top-middle 5 is visible from the top and right.
  - The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
  - The left-middle 5 is visible, but only from the right.
  - The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
  - The right-middle 3 is visible from the right.
  - In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.
Consider your map; how many trees are visible from outside the grid?
"""

from collections import namedtuple
Grid = namedtuple("Grid", "rows cols") 

testData = [
    "./problem_desc.txt",
    "./official.txt"
]


def getInput(input_file: str) -> list[str]:
    input = []
    with open(input_file, 'r') as df:
        while line := df.readline():
            input.append(line.strip('\n'))
    print(f"data file {input_file} has {len(input)} items")
    return input 


"""
"""


def createTreeGrid(input: list[str]) -> Grid:
    """
    instead of a list of lists to represent a grid,
    I'm going with a tuple of dicts, first dict is rows, second is columns.
    The dicts are indexed by row or column number.
    I think this makes it easier to grab each row and column to determine if an internal tree is visible.
    """
    grid = Grid({},{})
    for row, values in enumerate(input):
        grid.rows[row] = [int(v) for v in values]
        for col, val in enumerate(grid.rows[row]):
            """
            hang on, this gets a bit tricky.
            the lists for the columns don't yet exist (as we process the first row).
            We need them to exist because we're adding to each list with each value in a row.
            The index of the value in the row is the column that value belong to.
            Thus there's a check that will only really be needed on processing the first row, then ignored 
            """
            if not  grid.cols.get(col, None): grid.cols[col] = []    
            grid.cols[col].append(val)
    return grid 


def getGridDimensions(grid: Grid) -> tuple[int, int]:
    rows = len(grid.rows.keys())
    cols = len(grid.cols.keys())
    return (rows, cols)


def printGrid(input: str, grid: Grid) -> None:
    print(f"grid dimensions: {getGridDimensions(grid)}")
    print("-- Rows --")
    for row, vals in enumerate(grid.rows.values()): 
        print(f"row from input: {input[row]}")
        print(vals)
    print("-- Cols --")
    for col in grid.cols.values(): print(col)
    for i in input: print(i)


def iAmSomebody(grid: Grid, rowIdx: int, colIdx: int) -> bool:
    """
    if tree at rowIdx, colIdx can be seen from left, right, up, or down, return True.
    Return as soon as we know tree can be seen
    """
    row = grid.rows[rowIdx]
    col = grid.cols[colIdx]
    tree = row[colIdx]
    left = row[:colIdx]
    if tree > max(left): return True
    right = row[colIdx + 1:]
    if tree > max(right): return True
    down = col[:rowIdx]
    if tree > max(down): return True
    up = col[rowIdx + 1:]
    if tree > max(up): return True
    return False 


def main():
    for f in testData:
        input = getInput(f)
        grid = createTreeGrid(input)
        ## printGrid(input, grid)
        nrows, ncols = getGridDimensions(grid)
        """
        """
        seen = ((nrows - 1) * 2) + ((ncols - 1) * 2)
        for row in range(1, nrows - 1):
            for col in range(1, ncols - 1):
                if iAmSomebody(grid, row, col): seen += 1
        print(f"{seen} trees can be seen")


if __name__ == '__main__':
    main()


## end of file 