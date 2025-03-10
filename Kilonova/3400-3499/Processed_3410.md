
Consider an array of $n$ integers $a_1, a_2, a_3, \ldots, a_n$. A number $a$ is called moderate if it can be written as the product of two consecutive prime numbers, that is, $a = p_k \cdot p_{k+1}$, where $p_k, p_{k+1}$ are consecutive prime numbers.

# Task

1. A single number $a$ is given, determine if it is moderate.
2. An array of $n$ numbers is given, check for each number if it is moderate.

# Input data

The input file `moderat.in` contains:  
The first line contains the integer $c$ ($c = 1$ for task 1 or $c = 2$ for task 2).  
In the case of task $1$, one single number $a$ is read. In the case of task $2$, a number $n$ and an array of $n$ numbers are read.  

# Output data

The output file `moderat.out` must contain:  
For task $1$, print the number $a$ if it is moderate or $-1$ otherwise. For task $2$, for each number $a$ in the array, print the number $a$ if it is moderate or $-1$ otherwise, separated by a space.

# Constraints and clarifications

* $1 \le c \le 2$;
* $1 \le a_i \le 10^6$;
* $1 \le n \le 10^6$.

| # | Points | Constraints              |
|---|--------|--------------------------|
| 1 | 10     | For the examples provided. |
| 2 | 30     | $c = 1$                  |
| 3 | 30     | $c = 2$ and $1 \le n \le 100$ |
| 4 | 30     | $c = 2$ and $1 \le n \le 10^6$ |

# Example 1

`moderat.in`

```
1
15
```

`moderat.out`

```
15
```

## Explanation

Task $1$ checks the number: $15=3 \cdot 5$, so it is moderate, since $3$ and $5$ are prime numbers.

# Example 2

`moderat.in`

```
1
20
```

`moderat.out`

```
-1
```

## Explanation

Task $1$ checks the number: $20=2 \cdot 10=4 \cdot 5$, which cannot be written as a product of $2$ consecutive prime numbers.

# Example 3

`moderat.in`

```
2
5
6 10 15 35 77
```

`moderat.out`

```
6 -1 15 35 77
```

## Explanation

Task $2$ checks several numbers:  
- $6=2 \cdot 3$ is moderate;
- $10$ is not moderate;
- $15=3 \cdot 5$ is moderate;
- $35=5 \cdot 7$ is moderate;
- $77=7 \cdot 11$ is moderate.
