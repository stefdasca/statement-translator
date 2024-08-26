# String

Consider the alphabet consisting only of lowercase letters $a$ and $b$, and a string $S$ composed solely of characters from this alphabet. In this context, the inclusion relation is defined as follows: a string $S_1$ is included in string $S_2$ if the length of string $S_2$ (equal to the number of characters in the string) is greater than or equal to that of string $S_1$, and there exists a position $k$ in string $S_2$ such that $S_{2,k} = S_{1,1}$, $S_{2,k+1} = S_{1,2}$, $\dots$, $S_{2,k+L-1} = S_{1,L}$, where $L$ is the length of string $S_1$, $k+L-1$ is less than or equal to the length of string $S_2$, and $X_i$ represents the $i$-th character of string $X$. For example, the string `abba` is included in the string `babbaba`, but it is not included in the string `ababab`.

## Task

Determine the shortest string consisting only of characters from the considered alphabet that is not included in the string $S$.

## Input data

The first line of the input file `string.in` contains the integer $N$, representing the number of characters in the string $S$. The next line contains the $N$ characters, in the order of their positions in the string.

## Output data

The first line of the output file `string.out` will contain the integer $L$, representing the minimum length of a string that is not included in the string $S$. The second line will contain such a string. If there are multiple solutions, you can print any of them.

## Constraints

$1 \leq N \leq 500\ 000$

$0 < L$

## Example

`string.in`

```
11
aabaaabbbab
```

`string.out`

```
4
aaaa
```