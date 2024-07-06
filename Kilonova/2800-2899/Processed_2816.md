While Victor was walking through the forest, his attention was caught by a child playing on the sidewalk. The child was hopping from the first square, which had a number written on it with chalk, to another square with another number written on it, and so on until the $N$-th square at the end of the drawing. To make the game more interesting, his grandfather gave him the following challenge: He observed each number $A_i$ on the $i$-th square, with $1 \le i \le N$, and told him that, starting from the first square, at **each hop**, he will be given as many candies as the square of the difference between the number on the square he landed on and the number on the square he hopped from. More formally:
$nr_{candies} = (nr_{landed} - nr_{hopped})^2$ ,
with the meanings:
* $nr_{candies}$ = The number of candies his grandfather will give him at each hop
* $nr_{landed}$ = The number on the square he landed on
* $nr_{hopped}$ = The number on the square he hopped from

The boy can only hop forward and can stop hopping at any time he is satisfied with the number of candies obtained.

# Task

Knowing the number of squares, $N$, the numbers on each square, $A_1$, $A_2$, ..., $A_N$, and that the kid can hop a maximum of $K$ squares at any moment, calculate the **maximum number** of candies he can obtain.

# Input data

The first line of the input file `sarituri.in` contains two non-zero natural numbers, $N$ and $K$, with the meaning from the statement.  
The second line contains $N$ natural numbers, $A_1$, $A_2$, ..., $A_N$, with the meaning from the statement.

# Output data

The first line of the output file `sarituri.out` will contain a single natural number, which represents the **answer** to the given task.

# Constraints and clarifications

* $2 \le N \le 10^5$
* $1 \le K \le 10$
* $0 \le A_i \le 10^6$, with $1 \le i \le N$
* 10 points are awarded by default.

# Example 1

`sarituri.in`
```
4 1
3 6 1 2
```

`sarituri.out`
```
35
```

## Explanation

The child can hop at most one square, so the hopping sequence is:
$1 \rarr 2 \rarr 3 \rarr 4$:

~[sarituri_1.png|align=left|width=30%]

It is evident that the maximum sum is $(A_2 - A_1)^2 + (A_3 - A_2)^2 + (A_4 - A_3)^2$, which is equal to:  
$(6 - 3)^2 + (1 - 6)^2 + (2 - 1)^2 = 9 + 25 + 1 = 35$.

# Example 2

`sarituri.in`
```
5 2
2 3 8 7 2
```

`sarituri.out`
```
72
```

## Explanation

The child can hop at most two squares, so the hops can be:
* $i \rarr i + 1$
* $i \rarr i + 2$

It is observed that the sequence that achieves the maximum sum is:
$1 \rarr 3 \rarr 5$.

~[sarituri_2.png|align=left|width=30%]

Thus, the maximum sum is obtained: $(A_3 - A_1)^2 + (A_5 - A_3)^2$, which is equal to:  
$(8 - 2)^2 + (2 - 8)^2 = 36 + 36 = 72$