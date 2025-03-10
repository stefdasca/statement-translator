
# Task

You are given $n$, $k$, and then $k$ natural numbers. It is known that the sum of these $k$ numbers is $n$. Determine how many permutations of length $n$ exist with the property that they have exactly $k$ cycles, and the lengths of these cycles are exactly the given numbers.  
A cycle is defined as a subset of the permutation in which the elements swap places with each other. Example: $\{4, 2, 1, 3\}$, the permutation contains $2$ cycles $(4, 1, 3) (1 \rightarrow 4 \rightarrow 3 \rightarrow 1)$ and $(2)$.

# Input data

The first line of the input file `lencycles.in` contains two integers, $n$ and $k$.  
The second line contains the $k$ numbers representing the cycle lengths.

# Output data

The output file `lencycles.out` will contain a single integer representing the number of desired permutations, modulo $10^9+7$.

# Constraints and clarifications

* For tests worth 18 points, $1 \\leq n \\leq 10$;
* For other tests worth 42 points, $1 \\leq n \\leq 1000$ and it is guaranteed that the cycle lengths will be distinct numbers;
* For other tests worth 21 points, $1 \\leq n \\leq 100000$ and it is guaranteed that the cycle lengths will be distinct numbers;
* For other tests worth 19 points, $1 \\leq n \\leq 100000$;

# Example

`lencycles.in`
```
3 2
1 2
```

`lencycles.out`
```
3
```

## Explanation

We need to determine how many permutations of length $3$ have $2$ cycles, one of length $1$ and one of length $2$.  
There are a total of $6$ permutations of length $3$. Among these, only the permutations $(2, 1, 3)$, $(3, 2, 1)$, and $(1, 3, 2)$ have exactly $2$ cycles, one of length $1$ and one of length $2$.
```
