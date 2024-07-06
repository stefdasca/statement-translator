```markdown
Robot Vasile has to stick labels on products moving on a conveyor belt. The label of a product will contain its code, which is a natural number. Normally, the products should be coded with consecutive natural numbers starting from $1$, in increasing order. But Robot Vasile has a bug: it does not generate natural numbers that contain the natural number $X$ as a subarray.

A subarray is formed from digits located in consecutive positions in the number. For example, if $X = 213$, then the natural numbers $213$, $1213$, $2131$, $2132$ or $721389$ will not be generated because they contain $213$ as a subarray. However, the number $25136$ will be generated because the digits $213$ do not appear in consecutive positions.

# Task

Given $X$ and the number of products moving on the conveyor $N$, write a program to determine the code that will be on the label of the last product.

# Input data

The input file `bug.in` contains on the first line the natural numbers $X \\ N$, separated by a space, having the meaning given in the statement.

# Output data

The output file `bug.out` will contain a single line which will be written the code on the label of the last product on the belt (the $N$-th one).

# Constraints and clarifications

* $0 < X < 100\ 000$
* It is guaranteed that the digits of the number $X$ are distinct.
* $0 < N \leq 10^{16}$

|#|Score|Constraints|
|-|-|-|
|1|13|$1 \leq N \leq 10^6$|
|2|19|$10^6 < N$ and $X < 10$|
|3|24|$10^6 < N$ and $10 \leq X < 100$|
|4|44|$10^6 < N$ and $100 \leq X \leq 10^5$|

# Example

`bug.in`
```
3 13
```

`bug.out`
```
15
```

## Explanation

$X = 3$ and $N = 13$. The code on the label of the last product will be $15$, because the generated codes are $1$, $2$, $4$, $5$, $6$, $7$, $8$, $9$, $10$, $11$, $12$, $14$, $15$.
```