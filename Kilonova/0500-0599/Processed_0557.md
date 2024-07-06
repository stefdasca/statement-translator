*John has invested all his savings in cryptocurrencies. Now he is trying to recover some money by switching to the champion's diet (melted cheese).*

He has a circular container with $N$ pieces of cheese (of various types), and each day he takes one out of the container. He ensures that **before** and after taking a piece out of the container, any two adjacent remaining pieces are of different types.

John started counting the ways he can empty the container.

Formally, given a circular array $v_1, v_2, \ldots, v_N$, we want to remove one element at a time until the array is empty. After each removal, **including before the first removal**, no two consecutive positions in the array should have the same value.

~[bt.png|align=right|width=30%]

In the example on the right, the pieces of cheese on positions $A$ and $B$ have already been taken. The only pieces we could take now would be $E$ or $G$. If we took piece $C$, then pieces $D$ and $H$, both of type $2$, would become adjacent. If we took piece $D$, $C$ and $E$ would become adjacent, although they are both of type $1$, etc.

# Task
Count the number of ways we can empty the array respecting the rules (modulo $1\ 000\ 000\ 007$).

A way to empty the array is defined by the order of the indices that leave the array. For example, for $N = 4$, there are $4! = 24$ different ways to empty the array (not all of which comply with the rules given).

# Input data
The first line of the input file contains a single natural number $N$ representing the length of the array.

The second line contains $N$ natural numbers, $v_1, v_2, \ldots, v_N$, representing the values in the array.

# Output data
The output file will contain a single number, representing the number of ways to empty the array.

The problem has two scoring modes: the array is circular (for $100\%$ of the score on a test), or the array is not circular – $v_1$ and $v_N$ are not considered neighbors (for $80\%$ of the score).

Initially, the displayed number is compared with the corresponding answer for the circular array for $100\%$ of the test score.

If the answers differ, the number is then compared with the corresponding answer for the normal array ($v_1$ and $v_N$ are not considered neighbors) for $80\%$ of the test score.

# Constraints and clarifications
- $1\leq N \leq 500$
- $1 \leq v_i \leq N$

|# | Score | Constraints|
| - | - | ------------|
|1|10|$1\leq N\leq 10$|
|2|10|$1\leq N\leq 20$|
|3|30|$1\leq N\leq 50$|
|4|50|No additional constraints|

# Examples
`bt.in`
```
4
1 2 1 2
```
`bt.out`
```
0
```
Any element we take out, we would subsequently have two $1$s next to each other, or two $2$s next to each other, so we cannot empty the array. If there was a separator between the last and first elements, the answer would be $8$. The valid sequences of indices in this case would be:
- $1$, $2$, $3$, $4$
- $1$, $2$, $4$, $3$
- $1$, $4$, $2$, $3$ (the array would look like: $(1, 2, 1, 2) \rightarrow (2, 1, 2) \rightarrow (2, 1) \rightarrow (1) \rightarrow$ empty)
- $1$, $4$, $3$, $2$
- $4$, $1$, $2$, $3$
- $4$, $1$, $3$, $2$
- $4$, $3$, $1$, $2$
- $4$, $3$, $2$, $1$

`bt.in`
```
8
1 2 1 3 1 2 1 3
```
`bt.out`
```
1728
```
The correct answer if there was a separator is $6912$.

`bt.in`
```
4
1 2 3 4
```
`bt.out`
```
24
```
Since each element in the array is distinct, they can be taken out in any order. The answer for the other case is still $4! = 24$.

`bt.in`
```
6
1 2 3 1 3 2
```
`bt.out`
```
96
```
The correct answer if there was a separator is $312$.

`bt.in`
```
1
1
```
`bt.out`
```
1
```
We have only one element in the array, so there is only one way to take it out. The answer for the other case is still $1$.