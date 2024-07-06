Given a sequence $V$ consisting of $N$ integers $V_1, \dots , V_N$, we define a cut at position $pos$ as being a subarray that contains the element at position $pos$. Formally, the cuts at position $pos$ are in the form $V_k , V_{k+1}, ... , V_{pos} , ... , V_{r-1}, V_r$ for any $k$, $1 \leq k \leq pos$ and any $r$, $pos \leq r \leq N$.

The value of a cut is the sum of all elements that are part of that cut.

We define the function $\text{MulT}(pos)$ as being the number of cuts at position $pos$ that have a value of $0$.

# Task

Ioana, being very curious by nature, but also very fascinated by this function called $\text{MulT}$, is very interested in finding out the result for $\text{MulT}(i)$, where $1 \leq i \leq N$.

# Input data

The input file `taietura.in` contains on the first line a natural number $N$, representing the number of elements in the sequence $V$. The next line will contain exactly $N$ integer values separated by a space, namely the elements of the sequence $V$.

# Output data

The output file `taietura.out` will contain on the first line $N$ natural numbers separated by a space, namely the values of the function $\text{MulT}(i)$, where $1 \leq i \leq N$.

# Constraints and clarifications

- $1 \leq N \leq 100 \ 000$;
- Any element of the sequence $V$ is less than or equal in absolute value to $10^9$;
- For tests worth $20$ points, $N \leq 100$;
- For tests worth another $20$ points, $N \leq 1 \ 000$.

# Example 1

`taietura.in`
```
3
0 1 0
```

`taietura.out`
```
1 0 1
```

## Explanation

The result for $\text{MulT}(1)$ is $1$ because there is a single cut, namely $(0)$ that has the value $0$. For $\text{MulT}(2)$ the result is $0$ because there is no cut applied at position $2$ that has the value $0$. The result for $\text{MulT}(3)$ is $1$ because there is a unique cut, namely $(0)$ that has the value $0$.

# Example 2

`taietura.in`
```
6
2 -2 0 0 1 -1
```

`taietura.out`
```
4 4 6 6 4 4
```

## Explanation

For example, the result for $\text{MulT}(2)$ is $4$ because the cuts formed from the subarrays $(2, -2)$, $(2, -2, 0)$, $(2, -2, 0, 0)$, $(2, -2, 0, 0, 1, -1)$ have the value $0$.