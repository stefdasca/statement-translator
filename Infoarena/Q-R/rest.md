## Rest

Two natural numbers $N$ and $B$ and a sequence of $N$ numbers with natural values between $0$ and $B-1$ are given. Two types of operations can be performed on this sequence:
1. Modify an element: the element at position $x$ $(1 \leq x \leq N)$ takes the value $y$ $(0 \leq y < B)$.
2. Interval query: the remainder when dividing by $P$ of the number formed in base $B$ by concatenating the elements between positions $x$ and $y$ $(1 \leq x \leq y \leq N)$ is required.

## Task

For each query, display the required remainder.

## Input data

The first line of the file `rest.in` contains 3 natural numbers $N$, $B$, and $P$ as defined in the statement. The next $N$ lines contain each one element of the given sequence. Then follows the number $M$, which represents the total number of operations. The next $M$ lines contain 3 numbers each: $a$ $x$ $y$ ($a$ is 1 if the operation is a modification, 2 if the operation is a query), and $x$ and $y$ have the significance corresponding to each operation.

## Output data

The file `rest.out` will contain the answers to the queries, one number per line, in the given order.

## Constraints and clarifications

$1 \leq N, M \leq 250\,000$  
$2 \leq B, P \leq 30\,000$  
After concatenation, the most significant position in the obtained number is $x$, position $x+1$ is the next, $\dots$

## Example

`rest.in`

```
5 10 7 
1 
3 
9 
0 
7 
3 
2 2 3 
1 3 0 
2 3 5 
4 0
```

`rest.out`

```
0
```