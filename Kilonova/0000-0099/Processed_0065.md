```markdown
We are given `N` words composed only of the first `K` lowercase letters of the English alphabet and a sequence $x_i$ of `M` natural numbers. We need to form `M` words such that any word `i` `(1 \\leq i \\leq M)` satisfies the following properties:
* It has a length of $x_i$
* It is composed only of the first `K` lowercase letters of the English alphabet
* No word `cuv` among the initial `N` words or the other `M - 1` newly formed words can be a prefix of word `i`
* No word `cuv` among the initial `N` words or the other `M - 1` newly formed words can have word `i` as a prefix

# Task

Calculate the number of ways to form the `M` words that satisfy the properties mentioned above. Two ways are considered different if there exists at least one position `i` for which the `i`-th word is different. As this number can be very large, only the remainder when divided by `1 000 000 007` will be displayed.

# Input data
The first line contains `3` natural numbers separated by a space: `N, M` and `K`, having the meaning given in the statement. The next `N` lines contain one string each, representing the initial words. The last `M` lines contain one natural number $x_i$ each, representing the lengths of the words that need to be constructed.

# Output data
Print on a single line the number of ways to form the `M` words modulo `1 000 000 007`.

# Constraints and clarifications
* `1 \\leq N \\leq 300000`
* `1 \\leq M \\leq 300000`
* $1 \\leq x_i \\leq 300 \\ 000$, for any `1 \\leq i \\leq M`
* Let `S` be the sum of the lengths of the initial `N` words. Then `1 \\leq S \\leq 300000`
* `1 \\leq K \\leq 26`
* It is guaranteed that all initial words will be composed only of the first `K` lowercase letters of the English alphabet.

## Subtask 1 (8 points)
* `K = 2`
* $\\sum_{i=1}^M x_i \\leq 18$
* `S \\leq 20`

## Subtask 2 (19 points)
* $1 \\leq N, M, S, x_i \\leq 1000$

## Subtask 3 (11 points)
* `1 \\leq N, S \\leq 1000`
* $1 \\leq M, x_i \\leq 300 \\ 000$

## Subtask 4 (12 points)
* $x_i >$ length of any initial word among the `N`, for any `1 \\leq i \\leq N`

## Subtask 5 (11 points)
* `M = 1`

## Subtask 6 (7 points)
* `N = 1`

## Subtask 7 (32 points)
* Without additional constraints

# Examples

`stdin`

```
4 2 2
ab
abaa
bbb
baaa
3
3
```

`stdout`

```
12
```

`stdin`

```
6 5 3
aab
aabcc
aabb
bbb
bb
aaaab
2
3
6
5
5
```

`stdout`

```
925829353
```

Explanations
---

In the first example, there are `4` possibilities to form a word of length `3`: `aaa, aab, bab, bba`, and `12` possibilities to form two words of length `3`.
```
