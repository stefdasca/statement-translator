# Subsequence 2

Bronzarel trains daily to become a great olympiad in informatics, with Zaharel as his mentor. Of course, their favorite source of problems is infoarena! Seeing Bronzarel very confident, Zaharel wants to test him with a new problem and says: "I will give you a sequence of $N$ integers and I want you to tell me which is the shortest maximal increasing subsequence." 

## Task

Write a program that solves the given problem. 

## Input data

The first line from the file `subsir2.in` will contain the number $N$. The next line will contain $N$ integers. 

## Output data

The first line from the file `subsir2.out` will contain a number $L_{min}$, representing the minimum length of a maximal increasing subsequence. The next line will print $L_{min}$ numbers in increasing order, representing the positions of the elements from the initial array that are part of the chosen subsequence. If there are multiple solutions, the lexicographically smallest one, in terms of the values of the subsequence elements, will be printed. 

## Constraints and clarifications

$1 \leq N \leq 5\,000$

$50\%$ of the tests will have $N \leq 500$

The given sequence will contain integers in the interval $\left[-1\,000\,000, 1\,000\,000\right]$

Considering that the given sequence is $A=(a_1, a_2 \dots a_N)$, a subsequence of $A$ is called $B=(b_{i_1}, b_{i_2} \dots b_{i_N})$ with the property $1 \leq i_1 < i_2 < \dots < i_K \leq N$. We say that a subsequence $B=(b_{i_1}, b_{i_2} \dots b_{i_N})$ is maximal increasing if $a_{i_1} \leq a_{i_2} \leq \dots \leq a_{i_K}$ and there is not any $x$ such that:
- there exists $j < K$, $i_j < x < i_{j+1}$ and $a_{i_j} \leq a_x \leq a_{i_{j+1}}$, 
- or $1 \leq x < i_1$ and $a_x \leq a_{i_1}$ 
- or $i_K < x \leq N$ and $a_{i_K} \leq a_x$

For each test, $40\%$ of the score will be awarded for correctly determining the length of the subsequence, another $40\%$ for determining a correct solution, and an additional $20\%$ if the determined solution is lexicographically minimal.

A sequence $(x_1, x_2 \dots x_K)$ is lexicographically smaller than another sequence $(y_1, y_2 \dots y_K)$ if there is a position $p$ such that $x_p < y_p$ and $x_1 = y_1$, $x_2 = y_2$ $\dots$ $x_{p-1} = y_{p-1}$.

## Example

`subsir2.in`
```
6
1 3 6 2 5 4
```

`subsir2.out`
```
3
1 4 6
```

## Explanation

The subsequence with elements at positions $1, 4, 6$ is $(1, 2, 4)$. This is maximal and has the minimum length. Other maximal subsequences of the same length are: 
- $(1, 2, 5)$ 
- $(1, 3, 4)$ 
- $(1, 3, 5)$ 

The given solution is lexicographically minimal in terms of the values of the subsequence elements.