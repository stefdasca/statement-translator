
# Task

You are given an integer $N$, followed by $N$ positive numbers, the $i$-th number being $v_i$. Find the maximum *xor sum* that can be obtained by choosing a continuous subarray.

A subarray $(L, R)$ is defined as the sequence containing all values from the $L$-th to the $R$-th element, and its *xor sum* is given by $v_L \oplus v_{L+1} \oplus \dots \oplus v_R$, where $\\oplus$ is the XOR operator.

# Input data

The first line contains the integer $N$. The second line contains $N$ integers.

# Output data

The first line contains the required answer.

# Constraints and clarifications

* $1 \\leq N \\leq 2 \\cdot 10^5$
* $0 \\leq v_i \\leq 10^9$, $1 \\leq i \\leq N$

|#|Points|Constraints|
|-|-|-|
|1|20|$N \\le 500$|
|2|20|$N \\le 3\\ 000$|
|3|60|No additional constraints|

# Example 1

`stdin`
```
6
0 1 2 3 5 4
```

`stdout`
```
6
```

## Explanation

The subarray with the maximum *xor sum* is $(4, 5)$.

# Example 2

`stdin`
```
10 
1 2 100 12 3 0 12 4 0 1
```

`stdout`
```
107
```
