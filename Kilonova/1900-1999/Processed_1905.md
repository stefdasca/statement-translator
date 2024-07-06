> Somebody tell Lil Nas X

We call "$strinK$" a string $s$ of length $N$ ($2 \cdot K \leq N$), if there exists a subsequence of $2 \cdot K$ elements with indices $i_1, i_2, i_3, ..., i_{2 \cdot K}$, where $1 \leq i_1 < i_2 < i_3 < ... < i_{2 \cdot K} \leq N$ such that for any $j$, $1 \leq j \leq K$, $s_{i_{2 \cdot j - 1}}$ and $s_{i_{2 \cdot j}}$ are distinct.

For example, for $K=1$, the string $s=$ `abecc` is a "$strinK$", because the subsequence `ac` satisfies the condition described above (`a` and `c` are distinct).

# Task

For a string $s$ of length $N$ and a given number $K$, determine how many substrings are "$strinK$".

# Input data

The first line contains the natural numbers $N$ and $K$. The second line contains the string $s$.

# Output data

The first line contains a single integer representing the number of substrings that are "$strinK$".

# Constraints and clarifications

* $1 \leq K \leq 5 \cdot 10^5$;
* $2 \cdot K \leq N \leq 10^6$;

| # | Points | Constraints             |
| - | ------- | ----------             |
| 1 | 9     | $N \leq 100$    |
| 2 | 16      | $N \leq 2\ 000$     |
| 3 | 11      | It is guaranteed that $s_1=s_2$, $s_N=s_{N-1}$, and for $2 \leq i \leq N-1$, at least one of $s_{i-1}$ and $s_{i+1}$ is equal to $s_i$ |
| 4 | 27       | $N \leq 10^5$     |
| 5 | 37      | No additional constraints   |

$\bold{Attention!}$, during the contest the time limit was 0.1s, it was changed to 0.04s to encourage finding more efficient solutions. Submissions from the contest were not re-evaluated.

# Example 1
`stdin`
```
5 1
abecc
```

`stdout`
```
9
```

## Explanation

There are $9$ "$strinK$" substrings, $3$ of which are `abecc`, `be`, `abe`.

# Example 2
`stdin`
```
8 2
axbbcdde
```

`stdout`
```
11
```

## Explanation

There are $11$ "$strinK$" substrings, $4$ of which are `axbbcdd`, `xbbcd`, `bbcdde` and `cdde`.

# Example 3
`stdin`
```
8 3
axbbcdde
```
`stdout`
```
2
```

## Explanation

The only $2$ "$strinK$" substrings are `axbbcdde` and `xbbcdde`.