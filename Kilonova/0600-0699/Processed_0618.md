A natural number \( N \) is considered.

# Task

Determine all distinct perfect squares obtained by permuting the digits of the number \( N \). Examples:
- For \( N = 691 \), by permuting its digits we obtain the numbers \( 169 \), \( 196 \), \( 619 \), \( 691 \), \( 916 \), \( 961 \), from which 3 are perfect squares: 
  \( 169 = 13^2, 196 = 14^2 \) and \( 961 = 31^2 \).
- For \( N = 1044 \), by permuting its digits we obtain the numbers \( 1044 \), \( 1404 \), \( 1440 \), \( 4014 \), \( 4041 \), \( 4104 \), \( 4140 \), \( 4401 \), \( 4410 \), from which 2 are perfect squares: 
  \( 144 = 12^2 \) and \( 441 = 21^2 \).

# Input data

The input file contains the natural number \( N \) on the first line.

# Output data

The output file will contain on the first line the number \( P \) representing the number of perfect squares that can be obtained by permuting the digits of \( N \) and then the next \( P \) lines the \( P \) perfect squares in ascending order.
If there is no perfect square that can be obtained by permuting the digits of \( N \), the message *nu exista* will be displayed.

# Constraints

- \( 0 < N < 10^{14} \)
- Leading zeros in any permutation of \( N \) are not considered.

## Subtask 1 (20 points)
- \( 1 \le N < 10^4 \)

## Subtask 2 (68 points)
- \( 10^4 \le N < 10^{13} \)

## Subtask 3 (12 points)
- \( 10^{13} \le N < 10^{14} \)

# Example 1

`pcp.in`
```
691
```

`pcp.out`
```
3
169
196
961
```

# Example 2

`pcp.in`
```
1044
```

`pcp.out`
```
2
144
441
```

# Example 3

`pcp.in`
```
202050
```

`pcp.out`
```
4
225
2025
22500
202500
```

# Example 4

`pcp.in`
```
2023
```

`pcp.out`
```
nu exista
```