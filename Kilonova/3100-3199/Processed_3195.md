# Task

Given an array $a$ of $N$ elements.  
The cost of a continuous subarray $[st, dr]$ is $C(st, dr) = a_{st} \cdot (a_{st+1} + a_{st+2} + \ldots + a_{dr-1}) \cdot a_{dr}$.

Calculate $ \sum_{st=1}^{n-2} \sum_{dr=st+2}^n C(st, dr)$ modulo $10^9 + 7$.

# Input data

The first line contains $N$, and the second line contains $N$ values representing the array $a$.

# Output data

Print a single number, the required sum modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq N \leq 10^6$
* $1 \leq a_{i} \leq 10^9$
* For $20$ points, $1 \leq N \leq 150$.
* For other $30$ points, $1 \leq N \leq 5\ 000$.

# Example 1

`stdin`
```
4
2 1 3 2
```

`stdout`
```
28
```

## Explanation

$C(1, 3) = 6$  
$C(1, 4) = 16$  
$C(2, 4) = 6$  

# Example 2

`stdin`
```
8
7 45 12 4398 183 13261 423871 321
```

`stdout`
```
235372600
