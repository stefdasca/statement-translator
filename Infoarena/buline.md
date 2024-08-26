# Dots

Zaharel was bored during his college lectures and started drawing dots: he took $N$ tickets and drew a number of dots on each of them, either all white or all black. He arranged the $N$ tickets in a circle and asked himself the following question: if we consider that each ticket has an integer written on it ($x$ white dots will represent the number $x$, and $x$ black dots the number $-x$), what is the maximum sum of a sequence of tickets that are in consecutive positions?

## Input data

The input file `buline.in` will contain on the first line the natural number $N$. The next $N$ lines will contain two natural numbers, representing the number of dots on the tickets and their color ($0$ for black and $1$ for white), in the order they were arranged.

## Output data

The output file `buline.out` will contain three natural numbers: $S$ $P$ $L$ meaning that the sequence of tickets with maximum sum has a sum of $S$, starts at position $P$, and has a length of $L$. If there are multiple solutions, display the one with the smallest position $P$, and if there are multiple solutions with the smallest position $P$, display the one with the smallest length $L$.

## Constraints and clarifications

$1 \leq N \leq 200\ 000$  
The number of dots on a ticket is in the range $\[0, 10\ 000\]$  
The tickets are numbered from $1$ to $N$  
Considering the tickets are arranged in a circle, after ticket $N$ follows ticket $1$  
The chosen sequence must consist of at least one ticket  
For a test, $50\%$ of the score will be awarded for a correct solution, even if the values of $P$ or $L$ are not minimal  

## Example

`buline.in`  
```
5  
1 0  
2 1  
4 0  
3 1  
5 1  
```

`buline.out`  
```
9 4 4  
```

## Explanation

The 5 tickets, each having their number and dots:  
The tickets with the red outline form the sequence with the maximum sum.