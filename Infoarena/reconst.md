# Reconst

Rob and Halford have invented a game together. Rob thinks of an array of $N$ integers which Halford has to guess. Halford asks $M$ questions to Rob regarding the array of numbers, each question being in the form: "What is the sum of the numbers between positions $A$ and $B$ of the array?". Halford wants to find at least one array of $N$ integers for which all the answers provided by Rob to the $M$ questions are true.

## Input data

The input file `reconst.in` will contain on the first line 2 integers $N$ and $M$ having the meaning from the statement. The next $M$ lines contain information about the questions asked by Halford. Each line contains 3 integers $A$, $B$, and $S$ representing that the sum of the numbers between positions $A$ and $B$ inclusive of Rob's array is $S$.

## Output data

In the output file `reconst.out` you will print $N$ integers, representing an array for which all Rob's answers to the $M$ questions are true.

## Constraints and clarifications

$1 \leq N \leq 2000$

$1 \leq M \leq 2000$

$1 \leq A \leq B \leq N$

The elements of the array initially thought of by Rob are in the interval $[-1000, 1000]$

The displayed array must contain integers in the interval $[-2000\ 000\ 000, 2000\ 000\ 000]$

For all test files, there is at least one solution

Miruna did not contribute anything to this problem

## Example

`reconst.in`
```
3 3
1 2 5
2 3 7
1 3 8
```

`reconst.out`
```
1 4 3
```