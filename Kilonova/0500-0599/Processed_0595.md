Here is the translated competitive programming problem statement:

~[jolteon.png|align=right|width=30%]

Spark, the leader of the Instinct team, has gifted Jolteon an array $V$ of length $N$. Jolteon plays with this array by choosing subarrays and examining them closely. Being a Pokémon that detests neutrality, he defines a subarray as electrifying if, for every natural number $x$, one of these conditions is valid:
1. The number $x$ does not appear in the subarray, or
2. The number $x$ appears an odd number of times in the subarray.

Help Jolteon determine how many electrifying subarrays the given array contains.

# Implementation
Your program must implement the following function:
```cpp
long long solve(int N, int* V);
```

This function will be called once. The parameter $N$ represents the number of elements in the array. The parameter $V$ is an array of length $N$, **0-indexed**, containing the elements of array $V$. This function must return the number of electrifying subarrays of the array $V$.

# Testing
To test your solutions locally, we provide the program `main.cpp` and the header `jolteon.h`. The program `main.cpp` reads from the input file `jolteon.in`, calls the contestant's `solve` function, and prints the answer returned by it.

The input file `jolteon.in` contains:
The first line contains the natural number `N`. The second line contains `N` natural numbers, representing the elements of the array $V$. The output file `jolteon.out` contains the answer returned by the `solve` function.

# Constraints and clarifications
* $1 \leq N \leq 100\ 000$
* $1 \leq V[i] \leq 1\ 000\ 000$
* For `20%` of the tests, $N \leq 1\ 000$
* A subarray is understood to be a sequence of one or more elements found on consecutive positions in the original array.

# Example
`jolteon.in`
```
4
2 2 2 3
```
`jolteon.out`
```
7
```
Explanation
---
The electrifying subarrays are:
$[1, 1], [1, 3], [1, 4], [2, 2], [3, 3], [3, 4], [4, 4]$