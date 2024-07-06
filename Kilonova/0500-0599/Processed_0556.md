A great ancestor from Getae, Ziraxes, challenged the free Dacians to solve a programming problem, as it is a more pleasant activity than carrying boulders, pebbles, and sand. Legend says that on the elements of an array $A$ of non-zero natural numbers, the following operation can be performed:
- *Choose an element $A_{i}$ from the array and a natural number $x$ and subtract $x$ from $A_{i}$, so $A_{i}$ becomes $A_{i}-x$.*

The array $A$ is called *good* if, by applying the operation any number of times, the elements of the array $A$ become distinct non-zero natural numbers. For example, the array $2,3,3,5$ is good because by subtracting $2$ from the second element, it becomes $2,1,3,5$ and has distinct elements, whereas the array $2,2,7,2,4$ is not good.

# Task
Given an array $A$ with $N$ non-zero natural number elements, determine the number of subarrays in the array that are good. A subarray of the array is made up of elements from the array located at consecutive positions.

# Input data
The first line of the input file contains the number $N$, and the second line contains the elements of the array $A$.

# Output data
The output file will contain the number of subarrays in the array $A$ that are good.

# Constraints
- $1 \leq N \leq 100\ 000$.
- $1 \leq A_{i} \leq N$.

| # | Score | Constraints |
| - | - | ------------|
| 1 | 19 | $1 \leq N \leq 300$ |
| 2 | 20 | $1 \leq N \leq 1\ 500$ |
| 3 | 22 | $1 \leq N \leq 7\ 000$ |
| 4 | 17 | $1 \leq N \leq 50\ 000$ |
| 5 | 22 | No additional constraints |

# Example
`sirbun.in`
```
5
4 2 2 3 2
```
`sirbun.out`
```
13
```

The good subarrays are:
1) $\{4\}$
2) $\{2\}$
3) $\{2\}$
4) $\{3\}$
5) $\{2\}$
6) $\{4,2\}$
7) $\{4,2,2\}$
8) $\{4,2,2,3\}$
9) $\{2,2\}$
10) $\{2,2,3\}$
11) $\{2,3\}$
12) $\{2,3,2\}$
13) $\{3,2\}$