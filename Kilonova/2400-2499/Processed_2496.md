XORnelius is the best mathematician in the Kingdom of Info(1)cup. One day, he encountered a very interesting algorithmic problem. But instead of solving it, which would have been too simple for him, he decided to give it to you as a test.

# Task

You are given an array $a_0, a_1, \dots , a_{N-1}$ of numbers. For a continuous subarray $(i, j)$ of this array, we compute the _XORvalue_ of the subarray using the following steps:

1. Create an array $b$ of length $k = j - i + 1$, where $b_0 = a_i, b_1 = a_{i+1}, \dots b_{k-1} = a_j$.
2. The XORvalue is equal to the sum of values $(b_i \oplus i)^P$, for $0 \leq i < k$, where $ \oplus $ denotes the [XOR](https://en.wikipedia.org/wiki/Exclusive_or) operator.

You are required to calculate the sum of the XORvalues of all continuous subarrays of the array, modulo $10^9 + 7$.

More formally, if $f(i, j)$ is the XORvalue of the subarray $(i, j)$, then

$$
f(i, j) = \sum_{m = 0}^{j - i} (a_{i + m} \oplus m)^P
$$

You need to find the following value:

$$
\sum_{i = 0}^{N - 1} \sum_{j = i}^{N - 1} f(i, j) \ (mod\ 10^9 + 7)
$$

Your task is to solve this problem and show XORnelius that you are as good a mathematician as he is.

# Input data

The first line of the input data contains $N$, the length of the array, and $P$. The second line contains the values $a_0, a_1, \dots , a_{N-1}$.

# Output data

The single line of the output data must contain the required answer.

# Constraints

* $1 \leq N \leq 250 \ 000$
* $1 \leq P \leq 1 \ 000 \ 000 \ 000$
* $0 \leq a_i \leq 2^{18}$, for $0 \leq i < N$

| # | Points | Constraints            |
| - | ------- | -------------------   |
| 1 | 7       | $N \leq 100, P = 1$   |
| 2 | 8       | $N \leq 1\ 000, P = 1$|
| 3 | 12      | $N \leq 1 \ 000$      |
| 4 | 15      | $P = 1$               |
| 5 | 12      | $N \leq 50 \ 000, a_i < 8$, for $0 \leq i < N$ |
| 6 | 14      | $N \leq 50 \ 000, P = 2$ |
| 7 | 32      | No additional constraints         |

# Example 1

`stdin`
```
3 3
3 2 4
```

`stdout`
```
556
```

## Explanation

The XORvalues of all continuous subarrays of the array are written below.

* $i = 0, j = 0: b = \{3\}, f(0, 0) = (3 \oplus 0)^3 = 3^3 = 27$
* $i = 0, j = 1: b = \{3, 2\}, f(0, 1) = (3 \oplus 0)^3 + (2 \oplus 1)^3 = 3^3 + 3^3 = 27 + 27 = 54$
* $i = 0, j = 2: b = \{3, 2, 4\}, f(0, 2) = (3 \oplus 0)^3 + (2 \oplus 1)^3 + (4 \oplus 2)^3 = 3^3 + 3^3 + 6^3 = 27 + 27 + 216 = 270$
* $i = 1, j = 1: b = \{2\}, f(1, 1) = (2 \oplus 0)^3 = 2^3 = 8$
* $i = 1, j = 2: b = \{2, 4\}, f(1, 2) = (2 \oplus 0)^3 + (4 \oplus 1)^3 = 2^3 + 5^3 = 8 + 125 = 133$
* $i = 2, j = 2: b = \{4\}, f(2, 2) = (4 \oplus 0)^3 = 4^3 = 64$

The sum of all these values is equal to $556$ modulo $10^9 + 7$.

# Example 2

`stdin`
```
7 1
4 2 3 6 5 7 11
```

`stdout`
```
379
```

# Example 3

`stdin`
```
6 2
1 3 15 7 15 31
```

`stdout`
```
9410
