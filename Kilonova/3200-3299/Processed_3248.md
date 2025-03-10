
# Task

You are given a natural number $a$. We define the operation $swap$ on the number $a$ as the interchange of two adjacent digits. Formally, if $a$ has $n$ digits and the digits of the number $a$ are $a_1, a_2, \dots, a_n$, for an index $i (i \leq n-1)$, we define the operation as the interchange of the digit $a_i$ with $a_{i+1}$. Determine the maximum number that can be obtained after performing \textbf{at most } $k$ $swap$ operations on the number $a$.

# Input data

The first line of the input file `maximize.in` contains the natural number $a$.  
The second line of the input file contains the number $k$.

# Output data

The first line of the output file `maximize.out` will contain a single number, the maximized number $a$ after at most $k$ $swap$ operations.

# Constraints and clarifications

* Let $n$ be the number of digits of $a$.
* $1 \leq n \leq 1 \ 000$;
* $1 \leq k \leq 1 \ 000 \ 000$;
* Fewer than $k$ $swap$ operations can be performed on the number $a$, but not more than $k$.

|# | Score | Constraints|
| - | - | ------------|
|0|0|Example.|
|1|40|$1 \leq k \leq 1 \ 000$;|
|2|60|No additional constraints.|

# Example

`maximize.in`
```
30974
3
```

`maximize.out`
```
93704
```

## Explanation

If we apply the $swap$ operation, in order, for the digits $(a_2,a_3)$, $(a_1,a_2)$, and $(a_2,a_3)$, we obtain the number $93704$, which is the maximum that can be obtained from three $swap$ operations.
