# Rainbow

Miruna has $N-1$ houses arranged in a line, which she numbers from $1$ to $N-1$. Since she really likes brightly colored objects, she wants to perform $N-1$ color operations on the houses. Each operation is characterized by 3 values: $A_i$, $B_i$, and $C_i$, signifying that the new color of the houses between positions $\min(A_i, B_i)$ and $\max(A_i, B_i)$ is $C_i$. Starting from the second operation, Miruna uses the following recurrence relations:
$$A_i = (A_{i-1} \times i) \% N$$
$$B_i = (B_{i-1} \times i) \% N$$
$$C_i = (C_{i-1} \times i) \% N$$

## Task

You are asked to find the final color of each house.

## Input data

The first line of the `curcubeu.in` file contains 4 integers: $N$, $A_1$, $B_1$, and $C_1$, having the meaning described in the prompt.

## Output data

The `curcubeu.out` file will contain $N-1$ lines, with the number $i$ line containing a single integer representing the color of house $i$ after all the coloring operations are completed. If a house remains uncolored, the value $0$ will be printed.

## Constraints

$1 < N \leq 1\ 000\ 000$

$N$ will always be a prime number.

$1 \leq A_1 < N$

$1 \leq B_1 < N$

$1 \leq C_1 < N$

## Example

`curcubeu.in`
```
3 2 2 1
```

`curcubeu.out`
```
2
1
```