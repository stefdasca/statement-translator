## Task

Write a program that determines after how many time units no more turns are made.

## Input data

The first line of the file $soldati.in$ contains the integer $T$ representing the number of tests in the file. The following $T$ lines contain a sequence of characters from the set $\{ < , > \}$, which contains no spaces and ends with the end-of-line character. A character $<$ denotes a soldier facing left, and a character $>$ denotes a soldier facing right. The characters describing the soldiers are written in the order in which the soldiers are lined up (from left to right).

## Output data

For each of the $T$ tests, print in the output file $soldati.out$ a line containing an integer, representing the number of time units after which no more turns are made for the respective test.

## Constraints and clarifications

$1 \leq T \leq 10$

A line contains a maximum of $100\ 000$ characters from the set $\{ < , > \}$

For $20\%$ of the test files, the sequences will have a maximum of $1\ 000$ characters

## Example:

`soldati.in`
```
3
<<<>>>
>>>><
>>><<<
```

`soldati.out`
```
0
4
5
```