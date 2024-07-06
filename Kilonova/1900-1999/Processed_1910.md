> "Life is hard. It's better to skip all the hardships!"

Mux was in the park and found $t$ strings of $0$'s and $1$'s on a bench. He needs to find out how many *good* subarrays the string contains.
We define a subarray as *good* if the difference between the number of $0$'s and the number of $1$'s in the subarray is even. Note that this difference does not necessarily have to be positive.

# Task

Given $t$ strings, for each string specify how many subarrays have an even difference between the number of $0$'s and the number of $1$'s in the subarray.

# Input data

The first line contains the number $t$, and then on the $2 \cdot i$-th and the $2 \cdot i + 1$-th line $(1 \leq i \leq t)$ the length of the $i$-th string found by Mux and then the string itself.

# Output data

The $i$-th line $(1 \leq i \leq t)$ contains the answer to Mux's question for the $i$-th string.

# Constraints and clarifications

* $1 \leq t \leq 1\ 000$
* $1 \leq n \leq 10^6$, where $n$ is the length of each string.
* The string contains only the characters $0$ and $1$.
* The sum of the lengths of the $t$ strings of characters does not exceed $10^6$.
* **Note.** This problem has no connection with the problem [suxumetre](https://kilonova.ro/contests/34/problems/1906).

| # | Score | Constraints |
| - | ----- | ----------- |
| 1 | 0     | Example |
| 2 | 23    | $1 \leq n \leq 100$ |
| 3 | 36    | $1 \leq n \leq 1\ 000$ |
| 4 | 13    | The string contains only $0$ |
| 5 | 23    | No additional constraints |

# Example

`stdin`
```
4
9
010100100
7
0000000
18
100100010111010111
11
00000000000
```

`stdout`
```
20
12
81
30
```

## Explanation

For the first string, some of the subarrays that meet the required property are `0101`, `10`, `1001`, etc.