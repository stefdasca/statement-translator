Aurora likes permutations a lot. She defines a *kmax-permutation* as a permutation with the following property: for any subarray with elements in increasing order, the length of the subarray is at most equal to `k`. Now, Aurora wonders how many *kmax-permutations* with `N` elements exist.

# Task
Given the values of `N`, `k`, and `R`, find the number of *kmax-permutations* with `N` elements. The result will be calculated modulo `R`.

# Input data
The input file `kmax.in` will contain on the first line the natural numbers `N`, `k`, and `R`, having the meanings from the statement, separated by a space.

# Output data
The output file `kmax.out` will contain a single line which will print the number of *kmax-permutations* with `N` elements, modulo `R`.

# Constraints and clarifications
* $1 \leq k \leq N \leq 300$
* $10 \leq R \leq 30000$
* A subarray of a permutation is formed by elements located on consecutive positions.
* For `20%` of the tests `N \leq 10`
* For `60%` of the tests `N \leq 150`

# Example

`kmax.in`
```
4 2 997
```

`kmax.out`
```
17
```
Explanation
---

Among the `24` permutations of `4` elements, the following `7` are NOT 2max-permutations:
```
1 2 3 4
1 2 4 3
1 3 4 2
2 1 3 4
2 3 4 1
3 1 2 4
4 1 2 3
```

As observed, all the above seven permutations have at least one subarray with elements in increasing order of length greater than `2`.

`kmax.in`
```
30 10 27017
```

`kmax.out`
```
21690
```