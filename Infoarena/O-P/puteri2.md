# Powers of 2

Given a positive integer $N$, which is known to be of the form $x^P$ (with a given $P$), determine the value of $x$.

## Task

Find the value of $x$ for the given $N$ and $P$.

## Input data

The first line of the input file `puteri2.in` contains the integer $T$, representing the number of tests. 
The next $2T$ lines will describe the $T$ tests, with 2 lines for each test. The first line corresponding to a test contains the number $N$, while the second line contains the number $P$.

## Output data

For each test, print in the output file `puteri2.out` one line that contains the value of $x$.

## Constraints and clarifications

$1 \leq T \leq 30$ 

$1 \leq N \leq 10^{2000}$ 

$1 \leq P \leq 1000$

## Example

`puteri2.in`
```
4
4
2
1024
5
28561
4
9509900499
5
2
99
```
`puteri2.out`
```
2
4
13
4
```