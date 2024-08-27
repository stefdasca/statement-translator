# Iopds

Dubota is having trouble sleeping and dreams about subarrays. In her dream, our sheep walks on a path made of $N$ bricks, jumping from one brick to another. However, the bricks have real values written on them, $V_i$. Since Dubota is a subarray, she has a property, and after thinking thoroughly, she discovered this property is: $A * X_i^2 + B * X_{i-1}^2 + C * X_i * X_{i-1} > 0$. Now, the clever sheep wants to travel on the path such that the subarray formed by the values of the bricks she jumps on respects her property. Given the numbers $A$, $B$, $C$, and the array $V_i$ of $N$ numbers (representing the values of the bricks), help Dubota determine how many ways she can traverse the path.

## Input data

The input file `iopds.in` contains on the first line 3 real numbers, $A$, $B$, and $C$. The second line contains an integer, $N$. The third line contains $N$ real numbers representing the array $V$.

## Output data

In the output file `iopds.out`, you will print the number of subarrays that respect Dubota's property. Because this value can be very large, you will write it modulo $333019$.

## Constraints and clarifications

- $-1000 \leq A, B, C \leq 1000$
- $1 \leq N \leq 2000$
- $-10000 \leq V_i \leq 10000$
  
The values of $V_i$ are given with a precision of 3 decimal places. Assuming the given array is $V=(v_1, v_2, \dots, v_N)$, a subarray of $V$ is defined as a sequence $(v_{i1}, v_{i2}, \dots, v_{iK})$ with the property $1 \leq i_1 < i_2 < \dots < i_K \leq N$. Only subarrays containing at least 2 elements will be counted.

- For 30% of the tests $N < 12$.
- For 30% of the tests $A = B = 0.000$ and $C > 0.000$.

## Example

`iopds.in`
```
2.000 -1.000 1.000
6
3.000 4.000 -1.000 -1.000 0.000 -2.000
```

`iopds.out`
```
6
```

## Explanation

The bold values represent a subarray:
- $3.000\ 4.000\ -1.000\ -1.000\ 0.000\ -2.000$
- $3.000\ 4.000\ -1.000\ -1.000\ 0.000\ -2.000$
- $3.000\ 4.000\ -1.000\ -1.000\ 0.000\ -2.000$
- $3.000\ 4.000\ -1.000\ -1.000\ 0.000\ -2.000$
- $3.000\ 4.000\ -1.000\ -1.000\ 0.000\ -2.000$
- $3.000\ 4.000\ -1.000\ -1.000\ 0.000\ -2.000$