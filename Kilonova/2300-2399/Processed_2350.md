
Four sequences of real numbers are given $(a_n)_{n \geq 0}$, $(b_n)_{n \geq 0}$, $(c_n)_{n \geq 0}$, $(d_n)_{n \geq 0}$, defined recursively as follows:

$a_0$ = $a + b\sqrt{2}$, where $a$, $b$ are integers  
$b_0$ = $c + d\sqrt{2}$, where $c$, $d$ are integers  
$c_0$ = $e + f\sqrt{2}$, where $e$, $f$ are integers  
$d_0$ = $g + h\sqrt{2}$, where $g$, $h$ are integers  
$a_{n+1}$ = $a_0 a_n + b_0 c_n$, $n \geq 0$  
$b_{n+1}$ = $a_0 b_n + b_0 d_n$, $n \geq 0$  
$c_{n+1}$ = $c_0 a_n + d_0 c_n$, $n \geq 0$  
$d_{n+1}$ = $c_0 b_n + d_0 d_n$, $n \geq 0$

# Task

Find the smallest non-negative integer $n$ for which $a_n d_n = b_n c_n$.

# Input data

The file `siruri.in` contains $a$, $b$, $c$, $d$, $e$, $f$, $g$, $h$, separated by single spaces.

# Output data

Write to the file `siruri.out` $n$, or $-1$ if no such $n$ exists.

# Constraints and clarifications

- $a$, $b$, $c$, $d$, $e$, $f$, $g$, $h$ are integers with at most $8$ digits in positional notation in base $10$.

# Example 1

`siruri.in`
```
0 0 0 0 0 0 0 0
```

`siruri.out`
```
0
```

## Explanation

Because $a_0 b_0 = (0 + 0\sqrt{2})(0 + 0\sqrt{2}) = 0 \times 0 = 0$ and $c_0 d_0 = (0+ 0 \sqrt{2})(0+ 0 \sqrt{2}) = 0 \times 0 = 0$.

# Example 2

`siruri.in`
```
1 0 0 0 0 0 1 0
```

`siruri.out`
```
-1
```

## Explanation

Because $a_n = d_n = 1 + 0 \sqrt{2} = 1$ and $b_n = c_n = 0 + 0\sqrt{2} = 0$, meaning $a_n d_n = 1 \times 1 = 1$ and $b_n c_n = 0 \times 0 = 0$, for any $n \geq 0$.
