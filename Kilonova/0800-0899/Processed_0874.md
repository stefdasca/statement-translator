
Consider a set $S$ containing $N$ strings formed from lowercase letters of the English alphabet.  

A string is called _interesting_ in relation to the other strings in the set if there does not exist another string in the set that contains it as a subsequence. For example, if the set $S$ contains the strings `abc`, `bde`, and `abcdef`, then the only *interesting* string is `abcdef` because `abc` and `bde` do not contain it as a subsequence. Moreover, `abc` and `bde` are subsequences of `abcdef`, thus they are not *interesting*.

# Task

Given a set $S$ consisting of $N$ strings, determine:

1. The longest string. If there are multiple strings of the same maximum length, determine the smallest lexicographically.
2. All the _interesting_ strings from the set $S$.

# Input data

The input file `interesant.in` contains on the first line two natural numbers $p$ and $N$, separated by a space. For all input tests, the number $p$ can only have the value $1$ or $2$. The next $N$ lines contain the strings, one per line.

# Output data

If the value of $p$ is $1$, **only Task 1 will be solved**.

In this case, the output file `interesant.out` will contain the longest string among those read. If there are multiple strings of the same length, the smallest lexicographically will be written.

If the value of $p$ is $2$, **only Task 2 will be solved**.

In this case, the output file `interesant.out` will contain on the first line a value $K$ representing the number of _interesting_ strings, and on the next $K$ lines, the *interesting* strings **in the order they appear in the input file**.

# Constraints and clarifications

* $2 \leq N \leq 200$
* The length of a string will be between $1$ and $5\ 000$.
* A subsequence of the string $C_0 C_1 C_2 \dots C_k$ is defined as a succession of characters $C_{i_1} C_{i_2} C_{i_3} \dots C_{i_k}$, where $0 \leq i_1 < i_2 < i_3 < \dots < i_k \leq k$.
* The input file **DOES NOT contain identical strings**.

| $p$ | Points  |
| -   | ------- |
| $1$ | 20      |
| $2$ | 80      |

# Example 1

`interesant.in`
```
1 5
abcacaaz
ad
abcacaad
acd
zyt
```

`interesant.out`
```
abcacaad
```

## Explanation

$p=1$

The input file contains $5$ strings.

`abcacaad` is the string of maximum length. The string `abcacaaz` has the same length, but it is larger lexicographically.

**Attention! For this test, only Task 1 is solved.**

# Example 2

`interesant.in`
```
2 5
abcacaad
ad
zayyt
acd
zyt
```

`interesant.out`
```
2
abcacaad
zayyt
```

## Explanation

$p=2$

`ad`, `acd` are subsequences of `abcacaad`, and `zyt` is a subsequence of `zayyt`.

**Attention! For this test, only Task 2 is solved.**