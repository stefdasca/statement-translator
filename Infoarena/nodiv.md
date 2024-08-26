# Nodiv

Aenag Lurtseam finally reached college, where he received his first assignment. This time he is faced with a new problem: he receives a natural number $N$ and is asked to write it as a sum of terms of the form $2^a 3^b$. Although the assignment initially seemed easy, he encountered a new constraint - the sum must not contain two different terms such that one divides the other. For example, $15 = 2^1 3^1 + 2^0 3^2$ is a valid decomposition, but $18 = 2^1 3^1 + 2^2 3^1$ is not.

## Task

Will Aenag Lurtseam manage to pass the year without retakes?

## Input data

The first line of the input file will contain the number $T$ of tests, followed by $T$ lines, each containing a number $N$, the number to be decomposed.

## Output data

The output file will contain $T$ lines, each having the following format: a number $K$, followed by $K$ pairs $(a, b)$ representing the number of terms in the decomposition, respectively the exponents of those $K$ terms.

## Constraints and clarifications

$1 \leq N \leq 2^{63} - 1$ 

$1 \leq T \leq 10^3$ 

## Example

`nodiv.in` 
```
3 
15 
16 
17 
```

`nodiv.out` 
```
2 1 1 0 2 
1 4 0 
2 3 0 0 2 
```

## Explanations

$15 = 2^1 3^1 + 2^0 3^2$ 

$16 = 2^4 3^0$ 

$17 = 2^3 3^0 + 2^0 3^2$ 

~[example.png]