# Sortari

Ion and Vasile are playing with numbers. They have an array of $N$ natural numbers and decide to perform $M$ operations on it. An operation consists of choosing two positions $i$ and $j$ such that $i \leq j$ and swapping their values in case the value at $i$ is greater than the one at $j$.

## Task

Write a program that determines (for multiple subtests) whether the operations chosen by Ion and Vasile will sort any array of $N$ numbers in ascending order, regardless of their initial arrangement.

## Input data

The first line of the input file `sortari.in` contains the number $T$ of tests, followed by the description of each test. Each test contains two numbers $N$ and $M$ on the first line, representing the number of elements in their array and the number of chosen operations, respectively. Next, there are $M$ lines, each containing two numbers $a_i$, $b_i$, describing the chosen positions for that operation.

## Output data

The output file `sortari.out` will contain $T$ lines, each containing the value 1 if the operations chosen by Ion and Vasile sort any array of length $N$ in ascending order, or 0 otherwise.

## Constraints and clarifications

$1 \leq N \leq 17$

$1 \leq M \leq 600$

## Example

`sortari.in`
```
2 
4 6 
1 2 
2 3 
3 4 
1 2 
2 3 
1 2 
3 2 
2 3 
1 2 
```

`sortari.out`
```
1 
0 
```