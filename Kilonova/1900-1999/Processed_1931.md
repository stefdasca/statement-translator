
For an array of numbers $A$, the following cost function is defined:
$$f(A) = 1 \cdot V_1 + 2 \cdot V_2 + \dots + K \cdot V_K$$, where $[V_1, V_2, \dots, V_K]$ are the distinct values of $A$, sorted in ascending order.

Given an array of $N$ natural numbers $A$, calculate the sum of applying the function $f$ on all subarrays of $A$ (i.e. $\sum_{i=1}^{n} \sum_{j=i}^{n} f(A[i \dots j])$), where $A[i \dots j]$ is the subarray from $i$ to $j$.

# Input data

The input file `sortall.in` contains in the first line the natural number $N$. The second line contains $N$ natural numbers separated by space, representing the elements of the array $A$.

# Output data

The output file `sortall.out` will contain the answer modulo $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $1 \leq N \leq 50 \ 000$
* $1 \leq V_i \leq N$
* For 10 points $1 \leq N \leq 1 \ 000$
* For another 15 points $1 \leq N \leq 5 \ 000$
* For another 20 points, it is guaranteed that the values in the array are distinct

# Example 1

`sortall.in`
```
3
1 3 2
```

`sortall.out`
```
35
```

# Example 2

`sortall.in`
```
8
4 3 4 4 7 1 2 1
```

`sortall.out`
```
861
```
