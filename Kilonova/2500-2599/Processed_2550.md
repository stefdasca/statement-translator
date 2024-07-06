# Task

Given an array of $N$ elements, we can perform the following operation as many times as we want (maximum $N-1$), starting initially with a null score:
- Choose two indices $i$ and $j$, with $i < j$, such that $i \oplus j$ ($i$ xor on bits with $j$) is a number of the type $k^5$.
- Add to our score the value: $v_i^{v_j} + v_i \cdot v_j + v_j^{v_i}$ modulo P.
- Set either $v_i$ or $v_j$ to 0, and the set index can no longer be used.

What is the maximum score we can obtain?

# Input data

The first line contains two integers, $N$ and $P$.
The next line contains the sequence of $N$ numbers.

# Output data

The first line will contain a single integer, the maximum score obtained.

# Constraints and clarifications

* $1 \leq N \leq 10^5$;
* $1 \leq P, v_i \leq 10^9$;
* The final result is not calculated modulo $P$, only the scores of the operations are.

# Example 1

`stdin`
```
3 4
1 2 3
```

`stdout`
```
3
```

## Explanation

We choose only once $i=2$, $j=3$ (we can do this because their xor is $1$ which is $1^5$). So the total score will be $2^3 + 2 \cdot 3 + 3^2 = 23$ and under modulo P it equals $3$. We cannot obtain a better score.

# Example 2

`stdin`
```
6 11
4 891 38 19 43 99
```

`stdout`
```
13
```

