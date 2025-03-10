# Task

You are given a matrix $m$ with $N$ rows and $M$ columns containing values. You are also given a sequence of $Q$ directions (north, west, south, east). Starting from a point $(x_0, y_0)$ and following all the given directions in order, a path $(x_1, y_1), (x_2, y_2), \dots, (x_Q, y_Q)$ will be formed. For each $i$ ($1 \leq i \leq Q$), display $m_{x_1, y_1} + m_{x_2, y_2} + \dots + m_{x_i, y_i}$.

# Input data

The first line contains five integers, $N$, $M$, $Q$, $x_0$, and $y_0$. On the following $N$ lines, there are $M$ integers each, representing the values in the matrix. On the next line, there are $Q$ characters, which can be `N`, `E`, `S`, or `V`, representing the directions along which the path is constructed.

Due to the size of the input data, we recommend adding these lines at the beginning of the `main()` function:
```cpp
ios_base::sync_with_stdio(0);
cin.tie(0);
cout.tie(0);
```

# Output data

The first line should contain $Q$ numbers, representing the required sums.

# Constraints and clarifications

* $1 \leq N, M \leq 1 \ 000$
* $1 \leq Q \leq 100 \ 000$
* $1 \leq m_{i, j} \leq 1 \ 000 \ 000 \ 000$, where $1 \leq i \leq N$ and $1 \leq j \leq M$
* It is guaranteed that $1 \leq x_i \leq N$ and $1 \leq y_i \leq M$, where $0 \leq i \leq Q$.

# Example

`stdin`
```
3 4 8 2 3
1 2 3 4
5 6 7 8
9 10 11 12
SENVVNES
```

`stdout`
```
11 23 31 38 44 46 49 56
```

## Explanation

$m_{3, 3} = 11$  
$11 + m_{3, 4} = 23$  
$23 + m_{2, 4} = 31$  
$31 + m_{2, 3} = 38$  
$38 + m_{2, 2} = 44$  
$44 + m_{1, 2} = 46$  
$46 + m_{1, 3} = 49$  
$49 + m_{2, 3} = 56$