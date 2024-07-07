
# Task

We have an array $v$ of $N$ numbers, a $K$ and a $C$.

At most $K$ disjoint continuous subarrays are chosen. What is the maximum sum of the costs of the subarrays?
The cost of the subarray $[i \dots j] = (v[i]+v[j])^2+C+\sum_{p=i}^{j}v[p]$, $i < j$.

# Input data

The first line contains the numbers $N$, $K$ and $C$.
The second line contains the array $v$ of $N$ numbers.

# Output data

Print the maximum possible sum of the costs.

# Constraints and clarifications

* $1 \leq N \leq 10^5$;
* $1 \leq K \leq \left \lfloor{\frac{N}{2}}\right \rfloor $;
* $1 \leq v_i, C \leq 10^4$;
* Each chosen subarray must have at least $2$ elements.

# Example 1

`stdin`
```
5 2 1
2 3 1 2 1
```

`stdout`
```
44
```

## Explanation

We choose the subarrays $[1,2]$ and $[4,5]$, with costs of $(2+3)^2+1+2+3=31$ and $(2+1)^2+1+2+1=13$, in total $44$.

# Example 2

`stdin`
```
10 4 6
5 7 31 8 3 19 48 6 9 5
```

`stdout`
```
6764
```
