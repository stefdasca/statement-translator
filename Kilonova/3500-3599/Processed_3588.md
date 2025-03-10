**Suzi and Costel are participating in a multidisciplinary team competition. In the computer science section, they received a set $A$ consisting of $N$ integers. Each of them can only choose a single subarray from the sequence. Furthermore, these subarrays cannot overlap or be empty.**

They ask you to find the maximum value of dissimilarity between any two non-empty, non-overlapping subarrays from the set of $N$ integers in $A$.

The value of dissimilarity is defined as the absolute difference of the sums of the elements of the two subarrays.

# Input data

The first line contains an integer $N$, as described in the task.  
The second line contains $N$ integers, which are the values in the array $A$.

# Output data

Print a single integer, which is the maximum value of dissimilarity between any two non-empty, non-overlapping subarrays from the array $A$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$;
* $-10^9 \leq A_i \leq 10^9$, for $i=\overline{0,N-1}$.

|#|Points|Constraints|
|-|-|-|
|1|15|$N \leq 100$|
|2|25|$0 \leq A_i \leq 10^9$, for $i=\overline{0,N-1}$|
|3|60|No additional constraints|

# Example

`stdin`
```
5
7 3 -7 8 12 
```

`stdout`
```
27
```

## Explanation

In the example above, the maximum value of dissimilarity can be obtained by selecting the subarray $[-7]$ and the subarray $[8, 12]$. The dissimilarity value is $|(-7) - (8 + 12)| = |-7 - 20| = |-27| = 27$.