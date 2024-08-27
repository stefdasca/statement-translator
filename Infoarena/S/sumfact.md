## Task

A natural number $N$ is given. Write the number $N$ in the form $a_1 \cdot 1! + a_2 \cdot 2! + \dots + a_p \cdot p!$ such that $a_p$ is different from $0$ and the sum $a_1 + a_2 + \dots + a_p$ is minimal.

## Input data

The input file `sumfact.in` contains a single natural number, $N$.

## Output data

The output file `sumfact.out` will contain the decomposition of the number $N$ into a sum of factorials as follows: the first line will contain $P$, and each of the next $P$ lines will contain the value $a_i$.

## Constraints and clarifications

$1 \leq N \leq 2\ 000\ 000\ 000$

If there are multiple optimal solutions, you can display any of them.

## Example

`sumfact.in`  
130  

`sumfact.out`  
5  
0  
2  
1  
0  
1  

## Explanation

$0 \cdot 1! + 2 \cdot 2! + 1 \cdot 3! + 0 \cdot 4! + 1 \cdot 5! = 130$. Among all the possible ways to obtain this number, this one has the minimal sum of coefficients, $0 + 2 + 1 + 0 + 1 = 4$.