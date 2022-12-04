#!/usr/bin/env python

""" aoc2022/day01/part1.py 

https://adventofcode.com/2022/day/1

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

"""

testData = [
    "./problem_desc.txt",
    "./official.txt"
]

def getValue(line):
    try:
        return int(line)
    except ValueError as  ex:
        return -1


def findMaxCalories(input_file):
    print(f"using file: {input_file}")
    calories = 0
    max_calories =0
    elf = 1
    max_elf = 1
    with open(input_file, 'r') as df:
        while line := df.readline():
            if (cals := getValue(line)) > -1:
                calories += cals
            else:
                if calories > max_calories: 
                    max_calories, max_elf = calories, elf
                    print(f"new max: elf {elf} has {calories}")
                calories, elf = 0, elf + 1
    """
    if there was no newline after the last list of calories,
    the last elf will not be counted.
    checking here
    """
    if calories > max_calories: 
        max_calories, max_elf = calories, elf
        print(f"new max: elf {elf} has {calories}")

    print(f"and the winner is: elf {max_elf} has {max_calories}") 


def main():
    for f in testData:
        findMaxCalories(f)


if __name__ == '__main__':
    main()
    

## end of file 