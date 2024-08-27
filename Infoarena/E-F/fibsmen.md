# Fibsmen

Given a natural number $N$, determine in how many ways it can be written as the sum of distinct terms from the Fibonacci sequence. For every possible way, the order in which the terms are summed does not matter. Specifically, two ways that contain exactly the same terms will not be considered distinct and therefore will only be counted once. Answer $Q$ such questions.

## Input data

The input file `fibsmen.in` contains on the first line a single value $Q$ as described above. Each of the following $Q$ lines contains a single natural number $N$ which represents the value for which the respective question must be answered.

## Output data

The output file `fibsmen.out` will contain exactly $Q$ lines. The $i$-th line will contain the answer for the $i$-th question from the input file.

## Constraints and clarifications

$1 \leq Q \leq 200\,000$

$1 \leq N \leq 10^{16}$

## Example

`fibsmen.in`

```
3
6
73
666013
```

`fibsmen.out`

```
2
6
340
```

## Explanation

The $2$ distinct ways to write the number $6$ are: $1+2+3$ and $1+5$.

The $6$ distinct ways to write the number $73$ are: $2+3+13+21+34$, $2+3+5+8+21+34$, $5+13+21+34$, $2+3+13+55$, $2+3+5+8+55$ and $5+13+55$.