
# Task

You are given an array with $n$ natural numbers, with values **sorted in ascending order**. The task is to find the subarray with a sum of at least $k$ with the minimal difference between the maximum and minimum value in the subarray. If there are multiple such subarrays, find the one with the minimal length.

# Input data

The first line contains two integers, $n$ and $k$, representing the number of numbers in the array and the sum we want to reach.

The next line contains $n$ numbers **sorted in ascending order**, representing the values in the array.

# Output data

The first line will contain two numbers, representing the minimal required difference and the minimal length of a subarray that meets the specified property.

# Constraints and clarifications

* $1 \leq n \leq 200 \ 000$;
* $1 \leq k \leq 10^9$;
* $1 \leq v_1 \leq v_2 \leq \dots \leq v_n \leq 1 \ 000 \ 000$;
* A subarray represents the values in the array at some consecutive indices.
* It is guaranteed that there is at least one subarray with a sum of at least $k$.

# Example 1

`stdin`
```
7 10
2 3 3 4 4 5 7
```

`stdout`
```
1 3
```

## Explanation

The minimal difference is obtained if we take the subarray $(3, 3, 4)$, with a sum of $10$, the difference between the maximum and minimum being $1$ and the minimal length being $3$.

# Example 2

`stdin`
```
15 85
1 5 6 7 7 7 8 8 9 9 11 13 15 16 17
```

`stdout`
```
7 10
```

## Explanation

$6 + 7 + 7 + 7 + 8 + 8 + 9 + 9 + 11 + 13 = 85$
