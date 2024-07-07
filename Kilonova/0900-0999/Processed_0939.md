
We define the _distance_ between two strings of the same length as the minimum number of characters that need to be modified (each replaced by a different character) in the first string to obtain the second string. We denote the distance between the strings $a$ and $b$ as $dist(a, b)$.

For example, $dist($`abc`$,\\ $`aaa`$) = 2$ (we replace the character `b` with `a`, and the character `c` with `a`), and $dist($`ABC`$,\\ $`abc`$) = 3$ (lowercase letters are considered different from uppercase ones).

We define a _subarray_ of a string $s$ as a string formed from characters at consecutive positions in $s$. We consider two subarrays distinct if they start or end at different positions. We denote by $s(i, j)$ the subarray formed from the characters indexed from $i$ to $j$ of the string $s$. Strings are 0-indexed. Example: for the string $s = $ `abc`, the subarrays are $s(0, 0) = $ `a`, $s(1, 1) = $ `b`, $s(2, 2) = $ `c`, $s(0, 1) = $ `ab`, $s(1, 2) = $ `bc`, $s(0, 2) = $ `abc`, and for the string $s = $ `aa` they are $s(0, 0) =$ `a`, $s(1, 1) =$ `a`, $s(0, 1) =$ `aa`.

# Task

Given a string $s$, which can contain only lowercase and uppercase English alphabet letters (from `a` to `z` and from `A` to `Z`), for all unordered pairs of distinct subarrays of $s$ that have equal lengths, we want to calculate the distance between them and display their sum $\\text{mod }10^9 + 7$.

Formally, the task is to calculate the sum of the values $dist(s(a, b), s(c, d))$ for all indices $a$, $b$, $c$, $d$ with $0 \\leq a, b, c, d < |s|, a < c, a \\leq b, c \\leq d, b \ - a = d \ - c$, $\\text{mod }10^9 + 7$. $|s|$ denotes the length of the string $s$, which is 0-indexed.

# Input data

The file `sdistante.in` contains a single line with the given string $s$.

# Output data

Print a single integer on the sole output line of the file `sdistante.out`, representing the sum of distances, $\\text{mod }10^9 + 7$.

# Constraints and clarifications

* $|s| \\leq 4 \\ 000 \\ 000$, where $|s|$ is the length of the string $s$.
* For 11 points, $|s| \\leq 20$, $s$ contains only lowercase letters.
* For another 5 points, $|s| \\leq 50$, $s$ contains only the characters `a` and `b`.
* For another 15 points, $|s| \\leq 350$, $s$ contains only lowercase letters.
* For another 6 points, $|s| \\leq 1 \\ 000$, $s$ contains only the characters `a` and `b`.
* For another 30 points, $|s| \\leq 5 \\ 000$, $s$ contains only lowercase letters.
* For another 5 points, $|s| \\leq 100 \\ 000$, $s$ contains only the characters `a` and `b`.
* For another 4 points, $|s| \\leq 100 \\ 000$, $s$ contains only lowercase letters.
* For another 6 points, $|s| \\leq 1 \\ 000 \\ 000$, $s$ contains only the characters `a` and `b`.
* For another 18 points, there are no further constraints.

# Example 1

`sdistante.in`
```
abc
```

`sdistante.out`
```
5
```

## Explanation

* $dist(s(0, 0), s(1, 1)) = dist($`a`$,\\ $`b`$) = 1$
* $dist(s(0, 0), s(2, 2)) = dist($`a`$,\\ $`c`$) = 1$
* $dist(s(1, 1), s(2, 2)) = dist($`b`$,\\ $`c`$) = 1$
* $dist(s(0, 1), s(1, 2)) = dist($`ab`$,\\ $`bc`$) = 2$

# Example 2

`sdistante.in`
```
aab
```

`sdistante.out`
```
3
```

## Explanation

* $dist(s(0, 0), s(1, 1)) = dist($`a`$,\\ $`a`$) = 0$
* $dist(s(0, 0), s(2, 2)) = dist($`a`$,\\ $`b`$) = 1$
* $dist(s(1, 1), s(2, 2)) = dist($`a`$,\\ $`b`$) = 1$
* $dist(s(0, 1), s(1, 2)) = dist($`aa`$,\\ $`ab`$) = 1$

# Example 3

`sdistante.in`
```
ABa
```

`sdistante.out`
```
5
```

## Explanation

* $dist(s(0, 0), s(1, 1)) = dist($`A`$,\\ $`B`$) = 1$
* $dist(s(0, 0), s(2, 2)) = dist($`A`$,\\ $`a`$) = 1$
* $dist(s(1, 1), s(2, 2)) = dist($`B`$,\\ $`a`$) = 1$
* $dist(s(0, 1), s(1, 2)) = dist($`AB`$,\\ $`Ba`$) = 2$

# Example 4

`sdistante.in`
```
aaaaabbbaaaa
```

`sdistante.out`
```
480
```

# Example 5

`sdistante.in`
```
abcdefghizabcdefghiz
```

`sdistante.out`
```
7095
```
