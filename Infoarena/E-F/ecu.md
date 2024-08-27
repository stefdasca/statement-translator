# Ecu

Gigel has to solve a complicated system of nonlinear equations and intends to use an iterative method that, he hopes, will converge to a solution after a reasonable number of iterations. First, he chooses some initial values for the $N$ unknowns of the system. These values are denoted by $x_1^{(0)}$, $x_2^{(0)}$, $\dots$, $x_N^{(0)}$. Further, after each iteration, he will update the values of the unknowns according to the following relations: 
* $x_k^{(i)} = p_k \cdot x_k^{(i-1)} + (1 - p_k+1) \cdot x_{k+1}^{(i-1)} + y_k$ for $1 \leq k < N$ 
* $x_N^{(i)} = p_N \cdot x_N^{(i-1)} + (1 - p_1) \cdot x_1^{(i-1)} + y_N$ where $x_k^{(i)}$ denotes the value of the unknown $k$ after $i$ iterations. $p_k$ represents the weight associated with unknown $k$, and $y_k$ represents the correction applied to unknown $k$ after each iteration. Gigel is not a very good programmer and does not know how to implement the described iterative algorithm. Therefore, he needs your help.

## Task

Given the initial values of the $N$ unknowns, the associated weights, and the applied corrections, determine the values of the unknowns after $M$ iterations.

## Input data

The first line of the file `ecu.in` contains two integers, separated by a space, $N$ and $M$. The next line contains $N$ real numbers, representing the initial values of the unknowns, in the order $x_1^{(0)}$, $\dots$, $x_N^{(0)}$. The following line contains another $N$ real numbers, representing the weights associated with the unknowns, in order from $x_1^{(0)}$ to $x_N^{(0)}$. The last line of the file contains $N$ real numbers, describing the corrections that will be applied to the unknowns $x_1^{(0)}$, $\dots$, $x_N^{(0)}$, after each iteration. All real numbers are given with at most 3 decimals.

## Output data

The first line of the file `ecu.out` contains $N$ real numbers, rounded to three decimals, representing the values of the unknowns after $M$ iterations.

## Constraints and clarifications

$2 \leq N \leq 30$

$0 \leq M \leq 1\ 000\ 000\ 000$

$-1000 \leq x_i^{(0)} \leq 1000$, for $k$ from $1$ to $N$

$0 \leq p_k \leq 1$, for $k$ from $1$ to $N$

$-0.1 \leq y_k \leq 0.1$, for $k$ from $1$ to $N$

## Example

`ecu.in`
```
3 2 
1.0 2.0 3.0 
0.1 0.2 0.3 
0.001 0.002 0.003
```

`ecu.out`
```
2.173 1.765 2.075
```

## Explanation

After the first iteration, the values of the unknowns are: $1.701$; $2.502$; $1.803$. After the second iteration, the values of the unknowns are: $2.173$; $1.765$; $2.075$.