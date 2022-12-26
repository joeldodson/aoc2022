#!/usr/bin/env python

""" aoc2022/day08/part2.py 

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

--- Part Two ---

with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.
To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)
The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.
In the example above, consider the middle 5 in the second row:
30373
25512
65332
33549
35390
  - Looking up, its view is not blocked; it can see 1 tree (of height 3).
  - Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
  - Looking right, its view is not blocked; it can see 2 trees.
  - Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).
However, you can do even better: consider the tree of height 5 in the middle of the fourth row:
30373
25512
65332
33549
35390
  - Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
  - Looking left, its view is not blocked; it can see 2 trees.
  - Looking down, its view is also not blocked; it can see 1 tree.
  - Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.
Consider each tree on your map. What is the highest scenic score possible for any tree?
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
    name is Shout out to "The Jerk" (Steve Martin)...
    if tree at rowIdx, colIdx can be seen from left, right, up, or down, return True.
    Return as soon as we know tree can be seen
    """
    row = grid.rows[rowIdx]
    col = grid.cols[colIdx]
##     if row[rowIdx] != col[colIdx]: print(f"Error?? rowIdx: {rowIdx}, value: {row[rowIdx]}, colIdx: {colIdx}, value: {col[colIdx]}")
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

def viewScore(tree: int, view: list[int]) -> int:
    for idx, height in enumerate(view): 
        if height >= tree: return idx + 1
    return(len(view))


def howManyTreesCanISee(grid: Grid, rowIdx: int, colIdx: int) -> int:
    row = grid.rows[rowIdx]
    col = grid.cols[colIdx]
    tree = row[colIdx]
    view = 0
    left = row[:colIdx]
    left.reverse()
    right = row[colIdx + 1:]
    down = col[:rowIdx]
    down.reverse()
    up = col[rowIdx + 1:]
    score = (leftScore := viewScore(tree, left)) * (rightScore := viewScore(tree, right)) * (upScore := viewScore(tree, up)) * (downScore := viewScore(tree, down))
    ## print(f"tree at {rowIdx, colIdx}, height {tree}, has score: {score}, left len, score: {len(left), leftScore}, right len, score: {len(right), rightScore}, down len, score: {len(down), downScore}, up len, score: {len(up), upScore}")
    return score


def main():
    for f in testData:
        input = getInput(f)
        grid = createTreeGrid(input)
        maxView = 0
        ## printGrid(input, grid)
        nrows, ncols = getGridDimensions(grid)
        for row in range(1, nrows - 1):
            for col in range(1, ncols - 1):
                if (view := howManyTreesCanISee(grid, row, col)) > maxView: maxView = view 
        print(f"max view is {maxView} trees")


if __name__ == '__main__':
    main()


## end of file 