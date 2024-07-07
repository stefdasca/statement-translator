
A natural number $N$ is given and let $A$ be the set of all natural numbers between $1$ and $N^2$.

We call a partition of set $A$ a set of subsets $A_1, A_2, ..., A_N$ with the properties:

* The union of the $N$ subsets results in set $A$;
* The intersection of any two distinct subsets is the empty set;
* The number of elements of each subset $A_i$, $1 \leq i \leq N$, is $N$;
* The elements of each subset are placed in ascending order;

# Task

Write a program that determines a partition of the set $A$ with the properties:
* **The sums** of the elements of each subset $A_i$, $1 \leq i \leq N$, are equal;
* For any subset $A_i$, $1 \leq i \leq N$, **the difference** of any two successive elements is **different** from $N + 1$ and $N - 1$;

# Input data

The input file `partitie.in` contains on the first line the natural number $N$, as described above.

# Output data

The output file `partitie.out` will contain $N$ lines. Line $i$ will contain the elements of subset $A_i$, $1 \leq i \leq N$, separated by a space.

# Constraints and clarifications

* $5 \leq N \leq 1\ 000$;

# Example

`partitie.in`
```
5
```

`partitie.out`
```
1 8 15 17 24
3 10 12 19 21
5 7 14 16 23
2 9 11 18 25
4 6 13 20 22
```

## Explanation

$N = 5$;
$A = \{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25\}$
$A_1 = \{1,8,15,17,24 \}; 1+8+15+17+24 = 65$
$A_2 = \{3,10,12,19,21 \}; 3+10+12+19+21= 65$
$A_3 = \{5,7,14,16,23 \}; 5+7+14+16+23 = 65$
$A_4 = \{2,9,11,18,25 \}; 2+9+11+18+25 = 65$
$A_5 = \{4,6,13,20,22 \}; 4+6+13+20+22 = 65$

For all subsets $A_i$, $1 \leq i \leq 5$ the difference of any two successive elements is not $4$ or $6$ 
