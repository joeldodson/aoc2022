#!/usr/bin/env python

""" aoc2022/day06/part1.py 

https://adventofcode.com/2022/day/6

The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the star fruit grove.
As you move through the dense undergrowth, one of the Elves gives you a handheld device. He says that it has many fancy features, but the most important one to set up right now is the communication system.
However, because he's heard you have significant experience dealing with signal-based systems, he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.
As if inspired by comedic timing, the device emits a few colorful sparks.
To be able to communicate with the Elves, the device needs to lock on to their signal. The signal is a series of seemingly-random characters that the device receives one at a time.
To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.
The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position where the four most recently received characters were all different. 
Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.
For example, suppose you receive the following datastream buffer:
mjqjpqmgbljsphdztnvjfqwrcgsmlb
After the first three characters (mjq) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. Because j is repeated, this isn't a marker.
The first time a marker appears is after the seventh character arrives. Once it does, 
the last four characters received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is complete after 7 characters have been processed.
Here are a few more examples:
  - 
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
  - 
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
  - 
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
  - 
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
How many characters need to be processed before the first start-of-packet marker is detected?
"""

from parse import parse
from string import ascii_lowercase, ascii_uppercase


testData = [
    "./problem_desc.txt",
    "./official.txt"
]


SignalLength = 4

def getInput(input_file: str) -> list[str]:
    input = []
    with open(input_file, 'r') as df:
        while line := df.readline():
            input.append(line.strip('\n'))
    print(f"data file {input_file} has {len(input)} items")
    return input 


"""
lastSeen is the root of the algorithm.
As we iterate through the signal, we track the index of each letter.
for each letter, check against lastSeen when that letter was ... last seen
We also keep track of the potential start of the 4 unique letter sequence.
if the current letter lastSeen index is >= the unique tracker, 
we need to set the unique tracker to the index + 1 of the duplicated letter.
That is, if the current letter is 'x', at index 8,  with unique index == 5,
and 'x' was last seen at index 6, we need to set unique index to 7
"""
def findUnique(signal: str) -> int:
    ## print(f"signal is {signal}")
    lastSeen = {letter:-1 for letter in ascii_lowercase}
    uniqueStart = 0 
    for idx, letter in enumerate(signal):
        lsIndex, lastSeen[letter] = lastSeen[letter], idx
        if lsIndex >= uniqueStart: uniqueStart = lsIndex + 1
        elif idx + 1 - uniqueStart == SignalLength: return idx + 1  
    return -1 


def runTest(input: list[str]) -> None:
    for signal in input:
        firstChars = findUnique(signal)
        print(f"first {firstChars} are {signal[:firstChars]}")


def main():
    for f in testData:
        input = getInput(f)
        runTest(input)


if __name__ == '__main__':
    main()


## end of file 