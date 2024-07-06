Given an array $V$ of $N$ distinct natural numbers. A subarray $[X, Y]$ is formed from all the consecutive positions between $X$ and $Y$ in the array. The cost of a position $P$ is defined as the value in the array at position $P$ multiplied by the maximum length of a subarray that contains position $P$ and whose maximum value is also at position $P$.

# Task

You are given $M$ queries of the form: $X, Y$ – calculate the sum of all the costs of the positions in the subarray $[X, Y]$. **Attention!** When calculating the cost of a position $P$ in $[X, Y]$, the maximum length subarray where the value $V_P$ is maximum is calculated based on the entire array, **NOT** based on the subarray $[X, Y]$ (for clarification, see the example).

# Input data

The input file `secvcost.in` contains on the first line the two numbers $N$ and $M$, separated by space. The second line contains $N$ distinct natural numbers representing the elements of the array $V$. The next $M$ lines contain pairs of values $X, Y$ representing the queries that need to be answered.

# Output data

The output file `secvcost.out` will contain $M$ lines with one number on each line representing the answer to the $M$ queries, in order.

# Constraints and clarifications

* All values in the array are less than or equal to $5 \ 000 \ 000$

|#|Score|Constraints|
|-|-|--------|
|1|25|$1 \leq N, M \leq 500$|
|2|25|$1 \leq N, M \leq 10 \ 000$|
|3|50|$1 \leq N, M \leq 200 \ 000$|

# Example 1

`secvcost.in`
```
5 2
2 3 1 5 4
3 3
2 2
```

`secvcost.out`
```
1
9
```

## Explanation

For the first query we have $V_3 = 1$ which is maximum in the subarray $[3, 3]$. The cost is $1 \cdot 1 = 1$. For the second query we have $V_2 = 3$ which is maximum in the subarray $[1, 3]$. The cost is $3 \cdot 3 = 9$.

# Example 2

`secvcost.in`
```
5 3
2 3 1 5 4
1 3
5 5
4 4
```

`secvcost.out`
```
12
4
25
```

## Explanation

$2 \cdot 1 + 3 \cdot 3 + 1 \cdot 1 = 12$
$4 \cdot 1 = 4$
$5 \cdot 5 = 25$

# Example 3

`secvcost.in`
```
10 10
10 30 29 39 34 32 3 6 7 9
6 7
1 7
6 10
1 5
7 9
4 7
3 7
5 6
3 7
6 10
```

`secvcost.out`
```
163
886
232
723
36
757
786
364
786
232
```

## Explanation

523 \ 000