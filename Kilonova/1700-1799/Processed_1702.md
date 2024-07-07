
Consider a string $S$ composed of lowercase letters from the English alphabet. A subsequence of the string is palindromic if, when read from right to left, it results in the same word as when read from left to right.

# Task

Formulate $m$ queries of the form $i$, $j$, $k$ with the meaning: starting from the subsequence composed of the characters between indices $i$ and $j$ inclusive and with the possibility of extending it by at most $k$ characters in $S$ (immediately to the left of position $i$ and/or immediately to the right of position $j$), can we obtain a palindromic subsequence?

# Input data

The input file `sp.in` contains a string $S$ on the first line composed of lowercase letters from the English alphabet, not separated by spaces. The second line contains the number of queries $m$. Each of the following $m$ lines contains three numbers $i$, $j$ and $k$ (separated by spaces), representing the start index, the end index for a subsequence, and the maximum number of characters with which we can eventually extend it.

# Output data

The output file `sp.out` will contain a single line with $m$ values $0$ or $1$, not separated by spaces. If according to the $i$-th query, among the $m$ from the input file, we can form a palindrome under the conditions given, the $i$-th number in the output file will be $1$; otherwise, it will be $0$.

# Constraints and clarifications

* We denote by $n$ the length of the string $S$
* $1 \leq n \leq 200\ 000$
* $1 \leq m \leq 200\ 000$
* $0 \leq k \leq 5$
* For every query given in the form $i \ j \ k$, we have $1 \leq i \leq j \leq n$
* The string $S$ is 1-indexed.
* For tests worth $23$ points: $1 \leq n \leq 2\ 000$, $1 \leq m \leq 2\ 000$, and $k = 0$ for all queries.
* For other tests worth $11$ points: $1 \leq n \leq 2\ 000$, $1 \leq m \leq 2\ 000$.
* For other tests worth $45$ points: $1 \leq n \leq 2\ 000$, $1 \leq m \leq 200\ 000$.
* For other tests worth $21$ points, general constraints are maintained.

# Example

`sp.in`
```
abaaaac
6
1 2 0
1 2 1
2 4 1
2 4 2
1 2 0
2 2 1
```

`sp.out`
```
010001
```

## Explanation

In the first query, $k = 0$ and the given subsequence is not palindromic, so we output $0$.

In the second query with the same subsequence but now $k = 1$, we can extend it with one character. It can be extended by the character on the right, resulting in the subsequence `aba` which is palindromic.

In the third query, the subsequence formed `baa` is not palindromic, and by extending it with one character, we obtain the subsequences `abaa` (extending to the left) or `baaa` (extending to the right). Neither of these subsequences is palindromic.

In the fourth query, we have the subsequence `baa` and we can extend it by up to two characters: we have the options of extending it with one character from the left resulting in `abaa`, with one character from the right resulting in `baaa`, with one character from the left and one from the right resulting in `abaaa`, or with two characters from the right resulting in `baaaa`. We cannot extend by two characters to the left because we do not have enough characters.

The fifth query is the same as the first, so the result is $0$, and the sixth query contains an interval with a single element, which represents a palindromic subsequence.
