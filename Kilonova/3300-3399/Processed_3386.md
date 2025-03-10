# Task

Let $V$ be an array of $N$ numbers within the interval $[1, 1000]$. We say that an interval $[l, r]$ in the array is **good** if it meets the following conditions:

* $r - l \geq 2$
* for any $l \leq i < j \leq r, \ \ j - i \geq 2$, there exists a $c$ between $i$ and $j$ ($i < c < j$) such that $V_c = \dfrac{\text{max}(V_i, V_j)}{^\dagger \text{gcd}(V_i, V_j)}$.

$^\dagger \text{gcd}(a,b)$ = the greatest common divisor of numbers $a$ and $b$.

# Task

You are given $Q$ operations of the following types:

* $1 \ \ pos \ \ x \rightarrow a_{pos} = x$
* $2 \ \ l \ \ r \rightarrow$ find how many good intervals exist in $[l, r]$.

You need to answer all questions of type $2$. Operations of type $1$ are permanent.

# Input data

The first line contains two natural numbers, $N$ and $Q$. The next line contains the array $V$, followed by $Q$ lines representing the given operations.

# Output data

**The first line will print $Nr$, the number of good intervals present in the given array**. Subsequently, on separate lines, you will print the answers to the given questions.

# Constraints and clarifications

* $1 \leq N \leq 5 \cdot 10^5$;
* $1 \leq Q \leq 10^5$;
* It is guaranteed that '$x$' in the operations does not exceed $1 \ \ 000$.

| # | Score | Constraints |
| - | ----- | ------------ |
| 1 | 5 | $Q = 0, N \leq 10$ |
| 2 | 12 | $Q = 0, N \leq 1 \ \ 000$ |
| 3 | 23 | $Q = 0$ |
| 4 | 20 | $Q \leq 100$ |
| 5 | 12 | $1 \leq N \leq 10^5$ |
| 6 | 28 | No restrictions | 

# Example 1

`stdin`

```
6 0 
3 1 1 1 2 2
```

`stdout`

```
2
```

## Explanation

Only the intervals $[2,4]$ and $[4,6]$ are good.

# Example 2

`stdin`

```
10 8
1 1 1 1 1 1 1 1 1 1 
2 4 9
2 10 10
1 4 1
1 6 180
1 7 180
1 8 157
2 1 6
2 4 9
```

`stdout`

```
36
10
0
6
2
