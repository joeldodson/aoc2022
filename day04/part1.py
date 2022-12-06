#!/usr/bin/env python

""" aoc2022/day04/part1.py 

https://adventofcode.com/2022/day/4

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.
However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).
For example, consider the following list of section assignment pairs:
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:
  - 
Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
  - 
The Elves in the second pair were each assigned two sections.
  - 
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.
In how many assignment pairs does one range fully contain the other?
"""

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


def isSubset(elves:str) -> int: 
    e1l, e1u, e2l, e2u = [int(elu) for elu in elves.replace('-',',').split(',')]
    """
    this subset approach works fine but would be very inefficient for larger numbers.
    e1set = set(range(e1l, e1u+1))
    e2set = set(range(e2l, e2u+1))
    if e1set.issubset(e2set) or e2set.issubset(e1set): return 1
    else: return 0 
    """
    if (e1l >= e2l and e1u <= e2u) or (e2l >= e1l and e2u <= e1u):
        print(f"found subset: {elves}") 
        return 1
    else:
        return 0


def main():
    for f in testData:
        input = getInput(f)
        subsets = sum([issub for s in input if (issub := isSubset(s))])
        print(f"the total number of subsets is {subsets}")


if __name__ == '__main__':
    main()


## end of file 