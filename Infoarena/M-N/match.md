## Task

We will define a valid parenthesis sequence as a string of characters that can be:
* An empty string;
* A string $(B)$ where $B$ is a valid parenthesis sequence.
* $LR$, the concatenation of two strings $L$ and $R$, both being valid parenthesis sequences.

Let $B$ be a valid parenthesis sequence of length $N$. We will define $B(i)$ as the $i$-th character of the sequence $B$. For two indices $i$ and $j$, $1 \leq i < j \leq N$, we say that $B(i)$ and $B(j)$ form a parenthesis match if:
* $B(i) = '(' and $B(j) = ')$;
* $i = j-1$, or the subarray $C = B(i + 1)B(i + 2) \dots B(j - 1)$ is a valid parenthesis sequence.

Let $S$ be a string of lowercase letters from the English alphabet. We will define $S(i)$ as the $i$-th character of the sequence $S$. We say that a valid parenthesis sequence $B$ matches $S$ if:
* $B$ has the same length as $S$;
* For any pair of indices $i$ and $j$, $i < j$, if the parentheses $B(i)$ and $B(j)$ form a match, then $S(i) = S(j)$.

For a string $S$ consisting of $N$ lowercase letters, find the lexicographically smallest valid parenthesis sequence that matches $S$, or print $-1$ if such a sequence does not exist.

## Input data

The input file `match.in` contains a string $S$ of $N$ lowercase letters on the first line.

## Output data

In the output file `match.out` you will write a string $B$ of $N$ characters that represents the lexicographically smallest valid parenthesis sequence that matches the input string, or $-1$ if such a sequence does not exist.

## Constraints

$2 \leq N \leq 100000$

For tests worth 10 points, $N \leq 18.$

For tests worth 27 points, $N \leq 2000.$

A parenthesis sequence $A$ is said to be lexicographically smaller than the parenthesis sequence $B$ if there exists an index $i$, $1 \leq i \leq N$, such that $A_j = B_j$ for every $j < i$, and $A(i) < B(i)$. The character `'('` is considered lexicographically smaller than the character `')'`.

## Example

`match.in`
```
abbaaa
```

`match.out`
```
(()())
```

`match.in`
```
abab
```

`match.out`
```
-1
```

## Explanation

`abbaaa`

$(()())$

Another valid parenthesis sequence is $(())()$, but this is not the lexicographically smallest.

`abab`

$-1$

There is no valid parenthesis sequence that matches the given string.