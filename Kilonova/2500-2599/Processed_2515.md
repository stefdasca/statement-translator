```markdown
*The Mirror* of a natural number $x$ is the number obtained by reading the digits of $x$ from right to left, ignoring the trailing zeros of $x$. For example, the mirror of $103$ is $301$, while the mirror of $2500$ is $52$. A pair of distinct natural numbers $x$ and $y$ is called a *mirror pair* if both $x$ is the mirror of $y$, and $y$ is the mirror of $x$. For example, the numbers $x = 42$ and $y = 24$ form a mirror pair; however, the numbers $x = 1$ and $y = 100$ do not form a mirror pair.

A natural number $x$ is considered a *palindrome* if $x$ is equal to its mirror. For example, the number $42124$ is a palindrome. From two distinct numbers, a new number can be formed by appending one to the right of the other. For example, from the numbers $124$ and $42$, the numbers $12442$ (from appending $42$ to the right of $124$) and $42124$ (from appending $124$ to the right of $42$) can be obtained.

# Task

Given a sequence of natural numbers $a_1, a_2, ..., a_n$, determine:

1. The number of index pairs $(i, j)$, with $1 \le i \lt j \le n$, having the property that $a_i$ and $a_j$ form a mirror pair.
2. The largest palindrome that can be formed by appending two distinct numbers from the sequence.

# Input data

The file `perechi.in` contains:
 * The first line contains a natural number $C$, having the value $1$ or $2$, representing the task number.
 * The second line contains the natural number $n$.
 * The third line of the file contains the sequence of natural numbers $a_1, a_2, ..., a_n$, separated by spaces.

# Output data

The file `perechi.out` will contain a single number, representing the result corresponding to the given task.

# Constraints

* $1 \le C \le 2$
* $1 \le n \le 100 \ 000$
* $1 \le a_i \lt 10 \ 000$
* It is guaranteed that for task $1$ there is at least one mirror pair in the given sequence, and for task $2$ there is at least one palindrome number in the given sequence.

| # | Points | Constraints |
| - | - | ------------ |
| 1 | 27 | $C = 1$, $n \le 10 \ 000$ |
| 2 | 23 | $C = 1$, $10 \ 000 \lt n \le 100 \ 000$ |
| 3 | 27 | $C = 2$, $n \le 10 \ 000$ |
| 4 | 23 | $C = 2$, $10 \ 000 \lt n \le 100 \ 000$ |

# Example 1

`perechi.in`
```
1
5
21 12 21 12 21
```

`perechi.out`
```
6
```

## Explanation

There are $6$ index pairs with the property that their corresponding values form mirror pairs: $(1, 2), (1, 4), (2, 3), (2, 5), (3, 4)$ and $(4, 5)$. Each of these mirror pairs is composed of the values $12$ and $21$.

# Example 2

`perechi.in`
```
1
6
13 97 76 67 76 31
```

`perechi.out`
```
3
```

## Explanation

There are $3$ index pairs with the property that their corresponding values form mirror pairs: $(1, 6), (3, 4)$ and $(4, 5)$. These formed mirror pairs are: ($13, 31), (76, 67),$ respectively, $(67, 76)$.

# Example 3

`perechi.in`
```
2
6
24 79 42 97 123 124
```

`perechi.out`
```
42124
```

## Explanation

The following palindromes can be formed: $2442, 4224, 7997, 9779$ and $42124$. The largest among these is $42124$.
```