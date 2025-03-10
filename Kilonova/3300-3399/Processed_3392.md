
~[vasile.jpg|align=right|width=35%]

Vasile has a mustache of gigantic proportions and wants to trim it. His mustache can be seen as an array, $A$, of $N$ elements, where $A_i$ = the length of the $i$-th hair, $\forall i \in [0, N)$. We define the degree of ugliness of an interval $[l, r]$ as the difference between the longest and the shortest hair in the interval $[l, r]$.

# Task

Determine how many intervals $[l, r]$ exist such that the degree of ugliness is between $a$ and $b$.

# Input data

The first line contains the natural number $N$, as described in the statement.  
The second line contains the natural numbers $a$ and $b$, as described in the statement.  
The third line contains $N$ natural numbers, representing the array $A$.

# Output data

The first line will contain a single integer, representing the number of intervals $[l, r]$ for which the degree of ugliness is between $a$ and $b$.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $0 \leq a \leq b \leq {10}^{9}$
* $0 \leq A_i \leq {10}^{9}$
* For $30 \%$ of the tests: $N \leq 100$
* For $60 \%$ of the tests: $N \leq 1 \ 000$
* Recall that $A$ is indexed from $0$
* It is recommended to use fast I/O

# Example 1

`stdin`
```
6
4 5
1 7 5 4 2 6
```

`stdout`
```
5
```

## Explanation

$max([1, 4]) - min([1, 4]) = 7 - 2 = 5$  
$max([1, 5]) - min([1, 5]) = 7 - 2 = 5$  
$max([2, 5]) - min([2, 5]) = 6 - 2 = 4$  
$max([3, 5]) - min([3, 5]) = 6 - 2 = 4$  
$max([4, 5]) - min([4, 5]) = 6 - 2 = 4$  

# Example 2

`stdin`
```
5
0 0
1000000000 1000000000 1000000000 1000000000 1000000000
```

`stdout`
```
15
```

## Explanation

All intervals have a degree of ugliness $0$.
```
