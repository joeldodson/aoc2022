# Advent of Code, 2022

## Day 1

I took a bit of a brute force approach, not super pythonic.
As I read in the input, I kept a running sum of the calories for that elf.
Once done with that elf, compared to max value(s).
At least I didn't write my own sort algorithm.

Others in the RealPython slack channel did more with map and sum.
I like their solutions but mine scales to crazy large input, and I find it more readable.

## Day 2

I thought I'd take a more pythonic approach on day 2.
I decided it was quickest to configure some static maps for various points and game play results,
then again keep a running calculation as I read in the input.

## Day 3

Another figure out something and sum the input.
Maybe I should go more pythonic and functional on this one.

So I did.
Made more use of comprehensions and mapping methods (sum).
And had a good time with sets.
Resisted the temptation to cram it all into a single line though.

## Day 4

more sets...  subsets and non empty intersections.
Getting a bit more pythonic I guess.
And used lower and upper bound comparisons instead of sets this time.

## Day 5

A simple stack problem.
Reading in the input was most of the time.
used simple lists as stacks with append() and pop()

## Day 6

Pretty simple if you track the last time a character was seen.
lots of opportunity for off-by-one errors though.
Part 2 was literally changing a constant from 4 to 14

## Day 7

Spent way too much time worried about accommodating things like cd ../..
or multiple cd / commands in the input
Ditched that and it became a very simple tree navigation problem.

## Day 8
