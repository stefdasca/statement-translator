To determine the value of bits at specific positions in a binary sequence:

# Task
Given the natural numbers $N$ and $T$, as well as the natural numbers $p_1, p_2, \ldots, p_T$, determine the value of the bit at those positions in the obtained binary sequence.

# Input data
The input file contains on the first line the natural numbers $N$ and $T$, and on the second line, separated by spaces, the natural numbers $p_1, p_2, \ldots, p_T$.

# Output data
The output file will contain a succession of $T$ bits, without spaces, representing the answer to each query.

# Constraints and clarifications
- $1 \leq N \leq 100$
- $2 \leq T \leq 100\ 000$
- $1 \leq p_1, p_2, \ldots, p_T \leq 10^{18}$
- It is guaranteed that $p_1, \ldots, p_T$ will not be greater than the number of bits in the created sequence.

| # | Points | Constraints |
| - | - | ------------ |
| 1 | 7 | $N = 5$ and $p_1, \ldots, p_T \leq 10^9$ |
| 2 | 7 | $N \leq 20$ and $p_1, \ldots, p_T \leq 10^9$ |
| 3 | 26 | $N \leq 60$ and $p_1, \ldots, p_T \leq 10^{9}$ |
| 4 | 17 | $p_1, \ldots, p_T \leq 10^{5}$ |
| 5 | 26 | $p_1, \ldots, p_T \leq 5 \times 10^{10}$ |
| 6 | 17 | Without additional constraints |

# Examples
`trim.in`
```
3 10
7 1 2 3 4 5 6 8 9 10
```
`trim.out`
```
1111111101
```
We initially consider the numbers from $1$ to $7$. After applying the $trim$ operation and sorting, they become $1_2, 1_2, 1_2, 11_2, 11_2, 101_2, 111_2$. Therefore, after concatenation we get `1111111101111`, and the elements at the requested positions are those in the example.
\
`trim.in`
```
5 10
1 2 3 4 15 23 19 45 66 99
```
`trim.out`
```
1111011111
```
We initially consider the numbers from $1$ to $31$. After applying the $trim$ operation and sorting, they become
$1_2, 1_2, 1_2, 1_2, 1_2, 11_2, 11_2, 11_2, 11_2, 101_2, 101_2, 101_2, 1001_2, 1001_2, 10001_2, 111_2, 111_2, 111_2, \\\\ 1011_2, 1011_2, 1101_2, 1101_2, 10011_2, 10101_2, 11001_2, 1111_2, 1111_2, 10111_2, 11011_2, 11101_2, 11111_2$.

Therefore, after concatenation we get `1111111111111101101101100110011000111111111110111011110111011001110101110011111111110111110111110111111` and the elements at the requested positions are those in the example.