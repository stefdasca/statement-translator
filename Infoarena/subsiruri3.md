## Task

Aurel has an array of $N$ integers $x_1, x_2, \dots, x_N$. He wants to find out in how many ways he can choose a subsequence $x_{i_1}, x_{i_2}, \dots, x_{i_T}$ with the property that $0 \leq x_{i_j} - x_{i_{j-1}} \leq K$ for $j = 2 \dots T$. Help Aurel answer this question.

## Input data

The input file `subsiruri3.in` will contain on the first line $T$, the number of tests. Each test will contain on its first line two natural numbers, $N$ and $K$, with the meaning described in the task. The next line contains $N$ integers, separated by a space, representing Aurel's array.

## Output data

In the output file `subsiruri3.out` will be displayed $T$ lines, with the $i$-th line containing the number of subsequences with the property described in the task for test $i$, modulo $666013$.

## Constraints and clarifications

$1 \leq T \leq 5$

$1 \leq N \leq 10^6$

$0 \leq K \leq 10^9$

$0 \leq x_i \leq 10^9$ for $i = 1 \dots N$

A subsequence of the array $X = (x_1, x_2, \dots, x_N)$ is called $Y = (x_{i_1}, x_{i_2}, \dots, x_{i_T})$ with the property $1 \leq i_1 < i_2 < \dots < i_T \leq N$

## Example

`subsiruri3.in`

```
1
4 2
6 2 8 9
```

`subsiruri3.out`

```
7
```

## Explanation

The $7$ subsequences are: $\{6\}, \{2\}, \{8\}, \{9\}, \{6, 8\}, \{6, 8, 9\}, \{8, 9\}$.
