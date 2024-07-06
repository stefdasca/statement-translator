> "I'll send them later in the evening with a friend when the neighbors don't see you..."

# Task

The neighbor received a series of $n$ numbers from a friend. He wants to divide the series into subarrays of length at least 2, such that each number in the series appears in exactly one subarray. He then calculates the greatest common divisor of the numbers in each subarray and sums the obtained results, resulting in a sum $S$.

The neighbor realizes he can obtain different sums $S$, depending on how he divides the series into subarrays. Help the neighbor find the maximum possible sum $S$ he can obtain.

# Input data

The first line contains the number $n$. The second line contains $n$ space-separated numbers representing the numbers in the series.

Due to the size of the input data, we recommend adding these lines at the beginning of the `main()` function:

```cpp
ios_base::sync_with_stdio(0);
cin.tie(0);
```

# Output data

The first line will contain a single integer, the maximum possible sum $S$.

# Constraints and clarifications

* $2 \leq n \leq 200\ 000$;
* $1 \leq x \leq 2\ 000\ 000$, where $x$ is a number in the series;

| # | Points | Restrictions          |
| - | ------ | --------------------- |
| 0 | 0      | Example               |
| 1 | 30     | $n \leq 3\ 000$      |
| 2 | 70     | No additional restrictions |

# Example

`stdin`
```
5
6 2 3 1 4
```

`stdout`
```
3
```

## Explanation

The first subarray will be formed from the numbers $6, 2$; $gcd(6, 2) = 2$

The second subarray will be formed from the numbers $3, 1, 4$; $gcd(3, 1, 4) = 1$

$S = 2 + 1 = 3$

A larger sum cannot be obtained.