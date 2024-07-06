After FlaviuS mysteriously discovered that he is ambidextrous, he defined a boat of size $x$ as a string of characters that looks like this:

~[image.png|align=center]

For example, a boat of size $3$ looks like this: `\\\\\\___///` (`_` appears $3$ times). FlaviuS found, in addition to his quality, a string of $N$ characters, $S$, consisting only of the characters `\`, `_`, and `/`. He asks $Q$ questions of the form ($l$, $r$): What is the maximum size of a boat that is a subsequence of the subarray $S_l, S_{l+1} \dots, S_r$.

A subsequence is obtained from another string by deleting some characters while maintaining their order. For example, `\\_` is a subsequence of the string `\\/_/`, but `_\\` is not a subsequence of the string `\\/_/`.

# Input data

The first line contains two numbers, $N$ and $Q$, representing the length of the string and the number of questions FlaviuS asks. The second line contains the string $S$. The next $Q$ lines each contain two numbers $l$ and $r$.

# Output data

On line $i$, $1 \leq i \leq Q$, there will be a single number $x$, the maximum size of a boat.

# Constraints and clarifications

* $1 \leq N, Q \leq 10^6$
* $1 \leq l \leq r \leq N$ for each question
* If there is no boat in the chosen subarray, $0$ will be displayed.

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|9|$1 \leq N, Q \leq 200$|
|2|22|$1 \leq N, Q \leq 2 \ 000$|
|3|33|$1 \leq N, Q \leq 100 \ 000$|
|4|36|No other constraints|

# Example

`stdin`
```
17 6
\\_/\\/_\\___/_/\\/_/
1 2
1 3
1 17
3 10
2 16
5 10
```

`stdout`
```
0
1
3
0
2
0
```

## Explanation

In the first query, the subarray is `\\_`, so there is no boat.

In the second query, the subarray is `\\_/`, so there is a boat of size $1$.

In the third query, the subarray is the entire string. There is a boat of size $3$ formed by the characters at positions $1, 4, 7, 8, 9, 10, 11, 13, 17$. A boat of size $3$ looks like this: `\\\\\\___///`.