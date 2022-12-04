#!/usr/bin/env python

""" aoc2022/day01/part2.py 

https://adventofcode.com/2022/day/1#part2

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.
For example, suppose the Elves finish writing their items' Calories and end up with the following list:
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:
  - 
The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
  - 
The second Elf is carrying one food item with 4000 Calories.
  - 
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
  - 
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
  - 
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

PART 2:

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

testData = [
    "./problem_desc.txt",
    "./official.txt"
]

"""
topElves is an ordered list of dicts of the top N elves and calorie count for each.
"""
TopNElves = 3
## topElves = [{'elf':0, 'calories':0}  for i in range(TopNElves)]

def printTopElves(topElves):
    printString = f"the top {TopNElves} are "
    for elf in topElves:
        printString += f": elf {elf['elf']} with {elf['calories']} calories"
    printString += f", total calories is {sum([elf['calories'] for elf in topElves])}"
    print(printString)


def checkTopElves(topElves: list[dict], elf: int, calories: int) -> list:
    if calories > topElves[0]['calories']:
        topElves[0] = {'elf':elf, 'calories':calories}
        topElves = sorted(topElves, key = lambda d: d['calories'])
        printTopElves(topElves)
    return topElves 


def getValue(line: str) -> int:
    try:
        return int(line)
    except ValueError as  ex:
        return -1


def findMaxCalories(input_file):
    print(f"using file: {input_file}")
    topElves = [{'elf':0, 'calories':0} for i in range(TopNElves)]
    calories = 0
    elf = 1
    with open(input_file, 'r') as df:
        while line := df.readline():
            if (cals := getValue(line)) > -1:
                calories += cals
            else:
                topElves = checkTopElves(topElves, elf, calories)
                calories, elf = 0, elf + 1
    # make sure we didn't miss the last elf (no newline at end of file )
    topElves = checkTopElves(topElves, elf, calories)
    print("And the winners are...")
    printTopElves(topElves)

def main():
    for f in testData:
        findMaxCalories(f)


if __name__ == '__main__':
    main()
    

## end of file 